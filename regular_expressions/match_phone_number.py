import re

phone_numbers = input()

pattern = r"(\+359)([\- ])([2])(\2)(\d{3})(\2)(\d{4})\b"

filtered_numbers = re.finditer(pattern, phone_numbers)

print(", ".join([number.group() for number in filtered_numbers]))
