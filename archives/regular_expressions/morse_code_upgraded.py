import re

morse_codes = input().split("|")

for code in morse_codes:
    total = 0

    total += len(re.findall(r"0", code)) * 3 + len(re.findall(r"1", code)) * 5

    total += len("".join(re.findall(r"0{2,}|1{2,}", code)))

    print(chr(total), end="")
