import json

def read_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line.strip()) for line in file]

def process_data(data):
    result = []
    for entry in data:
        conversation_item = {
            "conversations": [
                {
                    "from": "human",
                    "value": f"<image>{entry['disease']}患者可以吃图中这道菜吗？"
                },
                {
                    "from": "gpt",
                    "value": entry['result']
                }
            ],
            "images":[
                entry['image']
            ]
        }
        result.append(conversation_item)
    
    return result

def write_json(output_path, data):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

input_file = ''  
output_file = '' 

jsonl_data = read_jsonl(input_file)
processed_data = process_data(jsonl_data)
write_json(output_file, processed_data)
print("ok!!")
