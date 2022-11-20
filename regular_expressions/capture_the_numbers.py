import re

pattern = r"\d+"
while True:
    strings = input()
    numbers = re.findall(pattern, strings)

    for number in numbers:
        print("".join(number), end=" ")
