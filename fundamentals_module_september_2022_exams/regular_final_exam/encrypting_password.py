import re

lines = int(input())

for password in range(lines):
    valid_password = re.search(r"^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1", input())

    if valid_password:
        encrypted_password = valid_password.group(2) +\
                             valid_password.group(3) +\
                             valid_password.group(4) +\
                             valid_password.group(5)

        print(f"Password: {encrypted_password}")

    else:
        print("Try another password!")
