import json
import random

try:
    with open("/Users/wilfried/Downloads/finetuning_shuffled_ds_v3.json", 'r') as json_file1:
        json1 = json.load(json_file1)
    print(len(json1))
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("/Users/wilfried/Downloads/finetuning_shuffled_exp_ds.json", 'r') as json_file2:
        json2 = json.load(json_file2)
    print(len(json2))
except Exception as e:
    print(f"An error occurred: {e}")

merged_json = []
for output_json in json1:
    info = output_json["output"]
    if info is None or "projects" in info:
        continue
    else:
        merged_json.append(output_json)

for output_json in json2:
    merged_json.append(output_json)

random.shuffle(merged_json)
print(f"Data Size: {len(merged_json)}")
refined_resume_section_file = "/Users/wilfried/Downloads/finetuning_shuffled_ds_v4.json"
with open(refined_resume_section_file, "w+", encoding='utf-8') as output_file:
    json.dump(merged_json, output_file, indent=4)