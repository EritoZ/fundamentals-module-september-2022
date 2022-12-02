import re

key_string = input()
text_string = input()

start_end_key = re.search(r"([A-Za-z]*)[|<\\].*?[|<\\]([A-Za-z]*)", key_string)

start = start_end_key.group(1)
end = start_end_key.group(2)

sentence = "".join(re.findall(rf"{start}(.*?){end}", text_string))

if sentence:
    print(sentence)
else:
    print("Empty result")
