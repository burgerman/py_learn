import csv
import json

# Define the input and output file paths
csv_file = "/Users/wilfried/Downloads/finetuning_resume_dataset.csv"
json_file = "/Users/wilfried/Downloads/finetuning_resume_dataset.json"
# Read the CSV file and convert to JSON
jobs = []
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        row["instruction"] = row["instruction"].replace("Generate a Resume", "Generate an improved resume to align the resume with the given job description while preserving the key information in the original resume data").strip()
        jobs.append({"input": row})

# Convert to JSON string and print
# json_output = json.dumps(jobs, indent=4)
with open(json_file, mode="w+", encoding="utf-8") as file:
    json.dump(jobs, file, indent=4)  # Save with indentation for readability

print(f"JSON file saved as {json_file}")