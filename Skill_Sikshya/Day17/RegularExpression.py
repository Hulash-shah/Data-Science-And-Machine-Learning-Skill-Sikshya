# Regular Expression In python

import re

# string = "The quick brown fox jumps over the lazy dog.My phone number is 987-654-3210 and my email is test@example.com."

# pattern = "brown"
# # re.search(pattern, string)
# match = re.search(pattern, string)

# if match:
#     print("Match Start: ", match.start())
#     print("Match End: ", match.end())
    
# string = "The quick brown fox jumps over the lazy dog.My phone number is 987-654-3210 and my email is test@example.com. ISU"

# pattern = "[A-Z]{2,}"

# match = re.findall(pattern, string)
# repl = "---"
# new_string = re.sub(pattern, repl , string , count = 0)
# print(new_string)

# print(match)
    
    

pattern = r"\[\d+\]" # [78] [90]

segments = re.split(
    pattern, 
    "Hello [78] , I am Wikipedia[2] ok",
    maxsplit = 0
)
print(segments)



