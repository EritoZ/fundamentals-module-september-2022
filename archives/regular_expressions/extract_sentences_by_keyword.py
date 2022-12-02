import re

word = input()
sentences = input()

pattern = rf"(?:(?<= )|^)[^.?!]*\b{word}\b[^.?!]*"

print("\n".join(re.findall(pattern, sentences)))
