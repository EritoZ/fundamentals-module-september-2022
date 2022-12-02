import re

skip_take = input().split()
a_string = input()

skip = int(skip_take[0])
take = int(skip_take[1])

pattern = rf"(?<=\|<).{{{skip}}}([^|<]{{,{take}}})"

print(", ".join(re.findall(pattern, a_string)))
