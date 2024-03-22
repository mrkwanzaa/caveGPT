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
api_message = ''

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

# def get_api():
#     global api_message
#     if api_message == '':
#         with connect(f'ws://localhost:8000/ws/?user_token={token}', max_size=None) as websocket:
#             websocket.send('{"command": "get_session_data","data": {"data_versions": {}}}')
#             for _ in range(4):
#                 message = websocket.recv()
#         api_message = message
#     return api_message

def get_api():
    global api_message
    if api_message == '':
        with open('api.json', 'r') as f:
            api_message = f.read()
    return api_message

def query_model(system, user, json):
    completion = client.chat.completions.create(
        model=api_model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        response_format={"type": "json_object"} if json else None,
    )
    return completion.choices[0].message.content

def find_top_level_key(command, error):
    message = 'Using the given documentation delimited by triple quotes, respond to user requests with nothing but the name of the top-level key that must be edited in order to fufill the request surrounded by single quotes' if error == False else \
        'Using the given documentation delimited by triple quotes, and an error message describing a potential issue, respond to user requests with nothing but the name of the top-level key that must be edited in order to fufill the request while avoiding the error surrounded by single quotes\n\nError: ' + error
    result = query_model(
        message,
        '"""' + docs_by_name['index'] + '""" \n\n' + 'request: ' + command,
        json=False
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
        'Using the given documentation delimited by triple quotes and current api state encoded in JSON, and an error message describing a potential issue, respond to user requests with the path(s) and value(s) you would modify in the api to achieve the users desired action while avoiding the error in the format \n```json\n{\"path\": example.path.here, \"value\": value}```. If the user request isn\'t possible with the given data respond with \'Not possible\'\n\nError: ' + error
    for data in chunks:
        result = query_model(
           message,
           data,
           json=True
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

read_json_file = lambda file: json.load(open(file, 'r'))

def find_prompt_test(prompt):
    tests = read_json_file('testCommands.json')
    for test in tests:
        if test['command'] == prompt:
            return test

prompts_dict = read_json_file('gptPrompts.json')
results = {}
passed = 0
if __name__ == '__main__':
    for prompt in list(prompts_dict.keys())[4:5]:
        results[prompt] = {}
        print(f'Prompt base: {prompt}')
        for command in prompts_dict[prompt]:  
            success = False
            error = False
            # accept command
            # command = input('Command: ')
            for k in range(10):
                try:
                    sleep(1)
                    old_api_key = None
                    for i in range(2):
                        api = json.loads(get_api())
                        print('Finding top level key...')
                        top_level_key = find_top_level_key(command, error)
                        print(top_level_key)
                        if top_level_key not in api['data'].keys():
                            error = f'{top_level_key} is not an acceptable key.'
                        else:
                            print('Chunking api...')
                            api_chunks = chunk_into_messages(command, top_level_key, api)
                            print('Finding mutation path...')
                            if old_api_key != top_level_key:
                                error = False
                            result = find_mutation_path(api_chunks, error)
                            print(result)
                            path = locate_path(result, top_level_key)
                            print(path)
                            print('Validating mutation')
                            api = pamda.assocPath(path=path['path'], value=path['value'], data=api['data'])
                            validator = Validator(api)
                            logs = validator.log.get_logs()
                            if len(logs) > 0:
                                error = logs[0]['msg']
                                print(logs)
                                print(f'Error encountered, attempting self correction')
                            else:
                                error = False
                                break
                    result = pamda.assocPath(path=path['path'], value=path['value'], data=api)
                    expected = find_prompt_test(prompt)

                    if pamda.path(expected['path'], api) == expected['value']:
                        success = True
                        break
                    else:
                        print('Mutation incorrect. Retrying...')
                except Exception as e: 
                    print(e)
            results[prompt][command] = success
            if success:
                print('Success!')
            # send_mutations(path, top_level_key, api['verions'])
    # save results to results.json
    with open('results.json', 'w') as f:
        json.dump(results, f)
        









