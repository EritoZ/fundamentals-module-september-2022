import re

string = input()
pattern = input()

count_pattern = len(re.findall(rf"\b{pattern}\b", string, re.IGNORECASE))

print(count_pattern)
