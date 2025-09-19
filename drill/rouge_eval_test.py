import json
try:
    with open("/Users/wilfried/Downloads/eval_project_ds.json", 'r') as json_file2:
        json2 = json.load(json_file2)
    print(len(json2))
except Exception as e:
    print(f"An error occurred: {e}")