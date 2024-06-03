# Imports and setup model
import os
import json
import re
import string
from time import sleep
from pamda import pamda
from cave_utils.api_utils.validator import Validator
from copy import deepcopy
import os
from openai import OpenAI
import configobj
import tiktoken
from time import sleep
import json

config = configobj.ConfigObj('.env')
client = OpenAI(api_key=config["OPENAI_API_KEY"])
model = 'gpt-4o-2024-05-13'
tokenizer_name = tiktoken.encoding_for_model(model)
tokenizer = tiktoken.get_encoding(tokenizer_name.name)

# Setup env vars and constants
docs_dir = 'docs/'

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

def get_api():
    global api_message
    if api_message == '':
        with open('api.json', 'r') as f:
            api_message = f.read()
    return api_message

def query_model(system, user, json):
    output = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system,
            },
            {"role": "user", "content": user},
        ],
        response_format={
                "type": "json_object",
            } if json else None,
    )
    return output.choices[0].message.content



def find_top_level_key(command, error):
    message = 'Using the given documentation delimited by triple quotes, respond to user requests with nothing but the name of the top-level key that must be edited in order to fufill the request surrounded by single quotes' if error == False else \
        'Using the given documentation delimited by triple quotes, and an error message describing a potential issue, respond to user requests with nothing but the name of the top-level key that must be edited in order to fufill the request while avoiding the error surrounded by single quotes\n\nError: ' + error
    result = query_model(
        message,
        '"""' + docs_by_name['index'] + '""" \n\n' + 'request: ' + command,
        False
    )
    result = result.replace('\n', '')
    current_key = re.sub(r'\W+', '', result)
    return current_key

def chunk_into_messages(command, top_level_key, api):
    max_tokens = 8000
    def add_request_text(api_data):
        return '"""' + docs_by_name[top_level_key] + '""" \n\n' \
                    + api_data + '\n\nrequest: ' + command
    state = api['data']
    encoded_data = json.dumps(state[top_level_key])
    encoded_chunk = add_request_text(encoded_data)
    chunks = [None]
    if tiktoken_len(encoded_chunk) > max_tokens:
        print('too long!')
        max_size = True
        key_dict =state[top_level_key]
        chunks[-1] = {i:key_dict[i] for i in key_dict if i!='data'}
        chunks[-1]['data'] = {}
        for key, value in key_dict['data'].items():
            # This isn't the exact token length as new data is outside request text, but should be within ~10 tokens
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
           True
        )
        if not 'Not possible' in result:
            return result
    return False

def extract_between_braces(s):
    open = 0
    indicies = []
    for i, char in enumerate(s):
        if open < 0:
            raise ValueError('Bracket mismatch')
        elif char == "{":
            if open == 0:
                indicies.append([i])
            open += 1
        elif char == "}":
            open -= 1
            if open == 0:
                indicies[-1].append(i)
    return [s[i[0]:i[1]+1] for i in indicies]

def follow_path(path_list, data):
    value = data
    for item in path_list:
        try:
            value = value[item]
        except:
            return None
    return value

def set_path(path_list, value, data):
    original = deepcopy(data)
    current = original
    for item in path_list[:-1]:
        try:
            current = current[item]
        except NameError:
            current[item] = {}
            current = current[item] 
    current[path_list[-1]] = value
    return original

def locate_path(path_string, top_level_key):
    filtered_json = extract_between_braces(path_string)
    paths = []
    for s in filtered_json:
        try:
            given_path = json.loads(s)
            list_path = given_path.get('path', "").split('.')
            if list_path[0] != top_level_key:
                list_path.insert(0, top_level_key)
            final_path = []
            for i in range(len(list_path)):
                if list_path[i].isdigit():
                    final_path.append(int(list_path[i]))
                else:
                    index = re.search("\[[0-9]\]", list_path[i])
                    if index is not None:
                        final_path.append(list_path[i].replace(index.group(), ''))
                        final_path.append(int(index.group().strip("[]")))
                    else:
                        final_path.append(list_path[i])
            given_path['path'] = final_path
            paths.append(given_path)
        except:
            print("Path failed, moving on")
    return paths

read_json_file = lambda file: json.load(open(file, 'r'))

def find_prompt_test(prompt):
    tests = read_json_file('testCommands.json')
    for test in tests:
        if test['command'] == prompt:
            return test

prompts_dict = read_json_file('QwenPrompts.json')
results = {}
passed = 0
if __name__ == '__main__':
    for prompt in list(prompts_dict.keys()):
        results[prompt] = {}
        print(f'Prompt base: {prompt}')
        for command in prompts_dict[prompt]:  
            success = False
            error = False
            # accept command
            # command = input('Command: ')
            for k in range(1):
                try:
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
                            paths = locate_path(result, top_level_key)
                            print(paths)
                            print('Validating mutation')
                            api = api['data']
                            for path in paths:
                                try:
                                    api = set_path(path['path'], path['value'], api)
                                except:
                                    print(f'Json failed: {path}')
                            validator = Validator(api)
                            logs = validator.log.get_logs()
                            if len(logs) > 0:
                                error = logs[0]['msg']
                                print(logs)
                                print(f'Error encountered, attempting self correction')
                            else:
                                error = False
                                break
                    result = set_path(path['path'], path['value'], api)
                    expected = find_prompt_test(prompt)

                    if follow_path(expected['path'], api) == expected['value']:
                        success = True
                        break
                    else:
                        if error:
                            print('caught error')
                        else:
                            print('uncaught error')
                except Exception as e: 
                    print(e)
            results[prompt][command] = success
            if success:
                print('Success!')
            # send_mutations(path, top_level_key, api['verions'])
    # save results to results.json
    with open('GptonQwenresults.json', 'w') as f:
        json.dump(results, f)
