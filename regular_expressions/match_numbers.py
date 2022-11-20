import re

text = input()

pattern = r"(^|(?<= ))(-)?(0|[1-9][0-9]*)(\.\d+)?($|(?= ))"

filtered_numbers = re.findall(pattern, text)

for number in filtered_numbers:
    print("".join(number), end=" ")
