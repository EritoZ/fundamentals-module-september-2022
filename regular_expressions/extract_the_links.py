import re

address_pattern = r"www\.[A-Za-z0-9\-]+\.[a-z]+(?:\.[a-z]+)*"
while True:
    text = input()
    valid_links = re.findall(address_pattern, text)

    if valid_links:
        print("".join(valid_links))
