# Imports and setup model
import os
from openai import OpenAI
import json
import configobj
import tiktoken
import asyncio
from websockets.sync.client import connect
from time import sleep
from pamda import pamda
from cave_utils.api_utils.validator import Validator

# Setup env vars and constants
config = configobj.ConfigObj('.env')
api_model = "gpt-4-1106-preview"
docs_dir = 'docs/'
client = OpenAI(api_key=config["OPENAI_API_KEY"])
token = config["CAVE_TOKEN"]


#Setup Tokenizer
tokenizer_name = tiktoken.encoding_for_model(api_model)
tokenizer = tiktoken.get_encoding(tokenizer_name.name)

# load docs
texts = []
docs_by_name = {}

for doc in os.listdir(docs_dir):
    with open(docs_dir + doc, 'r') as f:
        text = f.read()
        texts.append(text)
        docs_by_name[doc[0:-3]] = text

# Define functions
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)

def get_api():
    with connect(f'ws://localhost:8000/ws/?user_token={token}') as websocket:
        websocket.send('{"command": "get_session_data","data": {"data_versions": {}}}')
        for _ in range(4):
            message = websocket.recv()
    return message

def query_model(messages, json):
    completion = client.chat.completions.create(
        model=api_model,
        temperature=0.1,
        messages=messages,
        # max_tokens=200,
        response_format={"type": "json_object"} if json else None,
    )
    return completion.choices[0].message.content

def find_top_level_key(command):
    result = query_model([
            {"role": "system", "content": "Using the given documentation delimited by triple quotes, respond to user requests with nothing but the name of the top-level key that must be edited in order to fufill the request surrounded by single quotes"},
            {"role": "user", "content": '"""' + docs_by_name['index'] + '""" \n\n' + 'request: ' + command},
        ], json=False
    )
    current_key = result.replace("'", '')
    return current_key

def chunk_into_messages(command, top_level_key, api):
    max_tokens = 100000
    def add_request_text(api_data):
        return '"""' + docs_by_name[top_level_key] + '""" \n\n' \
                    + api_data + '\n\nrequest: ' + command
    state = api['data']
    encoded_data = json.dumps(state[top_level_key])
    encoded_chunk = add_request_text(encoded_data)
    chunks = [None]
    if tiktoken_len(encoded_chunk) > max_tokens:
        max_size = True
        key_dict =state[top_level_key]
        chunks[-1] = {i:key_dict[i] for i in key_dict if i!='data'}
        chunks[-1]['data'] = {}
        for key, value in key_dict['data'].items():
            # This isn't the exact token length as new data is outside request text, but should be within ~1 token
            if tiktoken_len(add_request_text(json.dumps(chunks[-1]))\
                            + json.dumps({key: value})) > max_tokens:
                chunks.append({i:key_dict[i] for i in key_dict if i!='data'})
                chunks[-1]['data'] = {key: value}
            else:
                chunks[-1]['data'][key] = value      
        for idx, chunk in enumerate(chunks):
            chunks[idx] = add_request_text(json.dumps(chunk))
    else:
        chunks = [add_request_text(encoded_data)]
    return chunks

def find_mutation_path(chunks, error):
    message = 'Using the given documentation delimited by triple quotes and current api state encoded in JSON, respond to user requests with the path(s) and value(s) you would modify in the api to achieve the users desired action in the format \n```json\n{\"path\": example.path.here, \"value\": value}```. If the user request isn\'t possible with the given data respond with \'Not possible\'' if error == False else \
        'Using the given documentation delimited by triple quotes and current api state encoded in JSON, and an error message describing a current issue, respond to user requests with the path(s) and value(s) you would modify in the api to achieve the users desired action in the format \n```json\n{\"path\": example.path.here, \"value\": value}```. If the user request isn\'t possible with the given data respond with \'Not possible\'\n\nError: ' + error
    for data in chunks:
        result = query_model([
            {"role": "system", "content": "Using the given documentation delimited by triple quotes and current api state encoded in JSON, respond to user requests with the path(s) and value(s) you would modify in the api to achieve the users desired action in the format \n```json\n{\"path\": example.path.here, \"value\": value}```. If the user request isn't possible with the given data respond with 'Not possible'"},
            {"role": "user", "content": data},
            ], json=True
        )
        if not 'Not possible' in result:
            return result
    return False

def send_mutations(path, top_level_key,  data_versions):
    with connect(f'ws://localhost:8000/ws/?user_token={token}') as websocket:
        command = {"command": "mutate_session"}
        command['data'] = {}
        command['data']['data_versions'] = data_versions
        command['data']['data_path'] = path['path']
        command['data']['data_value'] = path['value']
        command['data']['data_name'] = top_level_key
        websocket.send(json.dumps(command))

def locate_path(path_string, top_level_key):
    given_path = json.loads(path_string)
    list_path = given_path['path'].split('.')
    if list_path[0] != top_level_key:
        list_path.insert(0, top_level_key)
    given_path['path'] = list_path
    return given_path

if __name__ == '__main__':
    while True:   
        error = True
        # accept command
        command = input('Command: ')
        api = json.loads(get_api())
        print('Finding top level key...')
        top_level_key = find_top_level_key(command)
        print(top_level_key)
        print('Chunking api...')
        while error:
            api_chunks = chunk_into_messages(command, top_level_key, api)
            print('Finding mutation path...')
            result = find_mutation_path(api_chunks, error)
            path = locate_path(result, top_level_key)
            print(path)
            print('Validating mutation')
            api = pamda.assocPath(path=path['path'], value=path['value'], data=api['data'])
            validator = Validator(api)
            logs = validator.log.get_logs()
            if len(logs) > 0:
                error = logs[0]
                print(logs)
                # Note: remove this line to allow for unlimited re-attempts (could be expensive)
                input('Error encountered, press enter to try again')
            else:
                error = False
        send_mutations(path, top_level_key, api['verions'])









