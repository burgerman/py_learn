import json
import itertools


EDUCATIONS = """Instruction: Optimize the given "education" section of resume in JSON format. 
- Ensure integrity and consistency.
- Retain all provided details of education and degree, including institution names, degrees, dates, GPA. 
- Avoid missing or adding any educational details.
- Avoid hallucination.

<output_example>
"education": [
  {{
    "degree": "Masters of Science - Computer Science (Thesis)",
    "university": "Arizona State University, Tempe, USA",
    "from_date": "Aug 2023",
    "to_date": "May 2025",
    "grade": "3.8/4"
  }},
  {{
    "degree": "Bachelor of Science - Computer Science",
    "university": "Bangalore University, Bangalore, India",
    "from_date": "Aug 2019",
    "to_date": "May 2023",
    "grade": "3.6/4"
  }}
]
</output_example>

"""

PROJECTS = """Instructions: Improve the given "projects" section of resume in JSON format. 
- Retain listed projects in the resume.
- Improve clarity and alignment with the job requirements.
- Use clear, concise and professional language. 
- Format each project with bullet points.
- In each project description, it should include info, such as Task, Feature, Result.
- Avoid hallucination or adding details not given in the original resume data..

<output_template>
"projects": [
    {{
      "name": "project name1",
      "link": "https://devpost.com/software/project1",
      "from_date": "Nov 2023",
      "to_date": "Nov 2023",
      "description": [
        "introduction of project task, key features, and results."
      ]
    }},
    {{
      "name": "project name2",
      "link": "https://devpost.com/software/project2",
      "from_date": "June 2022",
      "to_date": "July 2022",
      "description": [
        "introduction of project task, key features, and results."
      ]
    }}
  ]
</output_template>

"""

SKILLS = """Instructions: Optimize the given "skill_section" section of resume in JSON format.
- Enhance the structure and alignment with the job description.
- Ensure most relevant skills in resume are retained.
- Add other relevant skills showed in other sections of resume if they are aligned with job requirements.
- Remove irrelevant details.
- Use precise and professional language.
- Avoid adding new skills that are not showed in resume.
- Avoid hallucination.

<output_example>
"skill_section": [
    {{
      "name": "Programming Languages",
      "skills": ["Python", "JavaScript"]
    }},
    {{
      "name": "Cloud and DevOps",
      "skills": [ "Azure", "AWS"]
    }}
  ]
</output_example>

"""

EXPERIENCE = """Instructions: Optimize the given "work_experience" section of resume in JSON format. 
- Format each project as the following output_example.
- In each experience, description should include information about responsibilities and impacts as string text.
- Improve clarity, structure, and alignment with the job description.
- Retain all important and relevant experience without altering factual details.
- Avoid adding details not given in the original resume data.

<output_example>
"work_experience": [
    {{
      "role": "Software Engineer",
      "company": "Winjit Technologies",
      "location": "Pune, India"
      "from_date": "Jan 2020",
      "to_date": "Jun 2022",
      "description": [
        "Engineered 10+ RESTful APIs Architecture and Distributed services; Designed 30+ low-latency responsive UI/UX application features with high-quality web architecture; Managed and optimized large-scale Databases. (Systems Design)",  
        "Initiated and Designed a standardized solution for dynamic forms generation, with customizable CSS capabilities feature, which reduces development time by 8x; Led and collaborated with a 12 member cross-functional team. (Idea Generation)" 
      ]
    }}
  ]
</output_example>

"""

SUMMARY = """Instructions: Optimize the given "summary" section of resume in JSON format. 
- Retain key details while enhancing clarity, conciseness, and alignment with the job description. 
- Ensure a strong, informative summary without adding new, unprovided content.
- Remove irrelevant and redundant content.
- No more than 100 words.
- Avoid hallucination

<output_example>
{{
  "summary": "Results-driven Marketing Professional with 5+ years of experience in digital marketing, brand strategy, and campaign management. Proven track record of increasing online engagement by 40% and driving a 25% boost in sales through data-driven strategies. Skilled in SEO, social media marketing, and analytics tools like Google Analytics and HubSpot. Passionate about creating innovative marketing solutions to help businesses grow. Seeking to leverage expertise in a dynamic, growth-oriented organization."
}}
</output_example>

"""



# json1 = [
#     "x1",
#     "x2"
# ]
try:
    with open("/Users/wilfried/Downloads/resume_ds.json", 'r') as json_file1:
        json1 = json.load(json_file1)
except Exception as e:
    print(f"An error occurred: {e}")

print(len(json1))
# json1_v2 = [{"resume": resume} for resume in json1]

# json2 = [
#     "job1",
#     "job2"
# ]

try:
    with open("/Users/wilfried/Downloads/job_ds.json", 'r') as json_file2:
        json2 = json.load(json_file2)
except Exception as e:
    print(f"An error occurred: {e}")

print(len(json2))

# json2_v2 = [{"job_description": job} for job in json2]

json3 = [
    PROJECTS,
    SKILLS,
    EXPERIENCE,
]

# Generate all combinations
merged_json = []

# for obj1, obj2, obj3 in itertools.product(json1, json2, json3):
#     merged_json.append({
#         "input": {
#             "resume": obj1,
#             "job_description": obj2,
#             "instruction": obj3
#         }
#     })

# for obj1, obj2 in itertools.product(json1, json2):
#     merged_json.append({
#         "input": {
#             "resume": obj1,
#             "job_description": obj2
#         }
#     })


# Output result
# print(json.dumps(merged_json, indent=2))


# filename = "/Users/wilfried/Downloads/merged_json_ds.json"
# try:
#     with open(filename, 'w+') as json_file:
#         json.dump(merged_json, json_file, indent=2)  # indent for readability
#     print(f"Data successfully written to {filename}")
# except Exception as e:
#     print(f"An error occurred: {e}")
