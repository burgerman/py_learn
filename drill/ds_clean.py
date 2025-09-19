import json

try:
    with open("/Users/wilfried/Downloads/inference_json_exp_ds.json", 'r') as json_file1:
        json1 = json.load(json_file1)
    print(len(json1))
except Exception as e:
    print(f"An error occurred: {e}")


cleaned_data = []

for instance in json1:
    for k in instance.get("output"):
        if "work_experience" in k:
            cleaned_data.append(instance)


print(f"Cleaned Data Size: {len(cleaned_data)}")
cleaned_file = "/Users/wilfried/Downloads/inference_json_exp_ds.json"
with open(cleaned_file, "w+", encoding='utf-8') as output_file:
    json.dump(cleaned_data, output_file, indent=4)
