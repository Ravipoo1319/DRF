import re

pattern = "^a...s$"
test_str = "abcds"

match_obj = re.match(pattern=pattern,string=test_str)

print(match_obj)

"""
re.match(pattern,string) => if pattern is matched then it returns match object
else returns None
"""

pattern = "^a...s$"
test_str = "Abcds"

match_obj = re.match(pattern=pattern,string=test_str)
print(match_obj)