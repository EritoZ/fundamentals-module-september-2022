import re

data_dict = {}

command = input()
while command != "END":
    data = re.findall(r"(?:\+|%20)*([^&?]+?)(?:\+|%20)*=(?:\+|%20)*(.+?)(?:\+|%20)*(?:(?=[&?])|$)", command)

    for field, value in data:
        field = re.sub(r"(?:\+|%20)+", " ", field)
        if field not in data_dict:
            data_dict[field] = []
        value = re.sub(r"(?:\+|%20)+", " ", value)
        data_dict[field].append(value)

    for field, value in data_dict.items():
        print(f"{field}=[{', '.join(value)}]", end="")

    print()
    data_dict.clear()

    command = input()
