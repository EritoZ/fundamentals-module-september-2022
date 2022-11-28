import re

text = input()

text = re.sub(r"\d+(?=[A-Za-z])", " ", text)
while " " in text:
    text = text.replace(" ", text[text.index(" ") + 1], 1)

print(text)
