import json
import re
import os


def add_jsonl_row(save_file, row):
    with open(save_file, 'a') as file:
        file.write(json.dumps(row) + '\n')

def add_jsonl_completion(save_file, model, completion):
    with open(save_file, 'r') as file:
        lines = file.readlines()

    if lines:
        last_object = json.loads(lines[-1].strip())
        if not last_object['result']:
            last_object['result'] = []
        last_object['result'].append({
            "model": model, 
            "result": completion
        })

        updated_last_line = json.dumps(last_object) + '\n'
        lines[-1] = updated_last_line
        with open(save_file, 'w') as file:
            file.writelines(lines)

def get_method_signature(code, method_name):
        method_def_prefix = "def " + method_name + '('
        code_segment = code.split('):')
        for segment in code_segment:
            if method_def_prefix in segment:
                return "    " + segment + "):"
        return ""

def openai_call(prompt, client, model="gpt-4o-mini", temperature=0, max_tokens=4096, top_p=1, frequency_penalty=0, presence_penalty=0, system_prompt = ""):
    response = client.chat.completions.create(
        model=model, 
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ], 
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty, 
        presence_penalty=presence_penalty,
        response_format={
            "type": "text"
        }
        
    )
    x= extract_python_code(response.choices[0].message.content)
    if not x: 
        return response.choices[0].message.content
    return x

def save_json(save_file, object):
    with open(save_file, 'w') as json_file:
        json.dump(object, json_file, indent=4)

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as json_file:
        for line in json_file:
            data.append(json.loads(line))
    return data

def merge_results(variants, generations, save=False, save_path='merged_files.csv'):
    """
    This method serves for giving folder for generations and model names, it merges them and return dicts. 
    """
    lengths  = []
    generations_results = []
    task_ids = []
    for g in generations:
        g_result = read_jsonl(os.path.join(g, 'result.json'))
        lengths.append(len(g_result))
        generations_results.append(g_result)

    assert len(set(lengths)) == 1
    generations_dict= {}
    f_generations_dict = {}


    for v in variants:
        generations_dict[v] = []
        f_generations_dict[v] = []
        
    

    for i in range(lengths[0]):
        task_id = generations_results[0][i]['task_id']
        task_ids.append(task_id)
        for j in range(len(generations_results)):
            results_ = generations_results[j][i]['result']
            assert task_id ==  generations_results[j][i]['task_id']
            prompt = generations_results[j][i]['prompt']
            for r in results_:
                generations_dict[r['model']].append(r['result'])
                f_generations_dict[r['model']].append(extract_python_method_code(prompt, r['result'])[0])
                
    if save: 
        df = pd.DataFrame(generations_dict, index=task_ids)
        f_df = pd.DataFrame(f_generations_dict, index=task_ids)
        df.to_csv(save_path, index_label='task_id')
        f_df.to_csv(f"f_{save_path}", index_label='task_id')
        
    return f_generations_dict, generations_dict, task_ids
        
def extract_python_method_code(start_code: str, generated_code: str) -> str:
    # Find the start index of start_code in generated_code
    start_index = generated_code.find(start_code)
    if start_index == -1:
        return ""

    # Define a regex pattern to match the method definition and its content
    main_pattern = re.compile(r'if\s+__name__\s*==\s*[\'"]__main__[\'"]:\s*\n.*', re.DOTALL)
    function_pattern = re.compile(
        rf'({re.escape(start_code)}(?:[\s\S]*?)(?=\n(?!\s)|\Z))',
        re.MULTILINE | re.DOTALL
    )
    # Define a regex pattern to match the def main() method and its content
    main_method = re.compile(r'def\s+main\s*\(.*?\)\s*:\s*\n(.*?)(?=\ndef\s+\w+\(|if\s+__name__|^\S|\Z)', re.DOTALL | re.MULTILINE)
    
    
    # Search for the code from start_code to the end of the method
    function_match = function_pattern.search(generated_code, start_index)
    if not function_match:
        return generated_code[start_index:].strip()

    # Extract the code from the start_code to the end of the method
    method_code = function_match.group(1).strip()
    # docstring_pattern = re.compile(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'')
    # method_code = docstring_pattern.sub('', method_code).strip()
    
    main_method_match = main_method.search(generated_code)
    main_match = main_pattern.search(generated_code)
    main_block = ''
    main_method_block = ''
    if main_match:
        main_block = main_match.group(0)
    if main_method_match:
        main_method_block = main_method_match.group(0)
        
    return method_code, main_method_block, main_block