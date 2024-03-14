from time import sleep
import json
from llama_cpp import Llama

def query_llama(prompt, llm):
    output = llm(prompt, echo=False, temperature=0)
    return output['choices'][0]['text']

read_json_file = lambda file: json.load(open(file, 'r'))
print(len(read_json_file('testCommands.json')))

llm = Llama(model_path="../llama-2-70b-chat.Q6_K.gguf", n_ctx=1300, n_threads=1, n_gpu_layers=1000)

results = {}

for command in read_json_file('testCommands.json'):
    print(command)
    result = query_llama(f'Restate the following command 10 times by rephrasing it using simpler language, writing the rephrasings as a json list of strings: {command["command"]}', llm)
    print(result)
    results[command["command"]] = result
    sleep(1)

with open(f'LLamaPrompts.json', 'w') as f:
            f.write(json.dumps(results))
