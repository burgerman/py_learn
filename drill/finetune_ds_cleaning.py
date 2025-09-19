import json
import random

try:
    with open("/Users/wilfried/Downloads/finetuning_training_exp_ds2.json", 'r') as json_file1:
        json1 = json.load(json_file1)
    print(len(json1))
except Exception as e:
    print(f"An error occurred: {e}")

merged_json = []
for json_instance in json1:
    for key in json_instance["output"]:
        output_list = json_instance["output"][key]
    # exp_list = json_instance["output"].get("work_experience")
    # skill_list = json_instance["output"].get("skill_section")
        if len(output_list) < 1:
            continue
        else:
            merged_json.append({
                "instruction":json.dumps(json_instance["input"]["instruction"]),
                "input": json.dumps({"resume":json_instance["input"]["resume"]}),
                "output": json.dumps(json_instance["output"])
            })



shuffled_list = random.sample(merged_json, len(merged_json))
print(len(shuffled_list))
shuffled_ds_file = "/Users/wilfried/Downloads/finetuning_shuffled_exp_ds.json"
with open(shuffled_ds_file, "w+", encoding='utf-8') as output_file:
    json.dump(shuffled_list, output_file, indent=4)