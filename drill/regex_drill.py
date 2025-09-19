import re

string_content = ""
pattern = re.compile("target pattern")
target_string = re.findall(pattern, string_content)
