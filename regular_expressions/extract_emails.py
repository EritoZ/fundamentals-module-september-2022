import re

string = input()

pattern = r"(?:(?<= )|^)(?:[a-z0-9]+[.\-_])?[a-z0-9]+@[a-z]+(?:[\-.][a-z]+)*\.[a-z]+"

valid_emails = re.findall(pattern, string)

for mail in valid_emails:
    print("".join(mail))
