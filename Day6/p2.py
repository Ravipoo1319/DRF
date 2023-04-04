import re

pattern = "[abc]"
test_str = "abc"

match_obj = re.search(pattern,test_str)

print(match_obj.group())