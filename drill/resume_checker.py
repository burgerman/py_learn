import json

try:
    with open("/Users/wilfried/Downloads/resume_ds.json", 'r') as json_file2:
        json_data = json.load(json_file2)
    print(len(json_data))
except Exception as e:
    print(f"An error occurred: {e}")


count = 0

for resume in json_data:
    projects = resume.get('projects')
    if projects is None or len(projects) < 1:
        count += 1
print(count)
print(count/len(json_data))