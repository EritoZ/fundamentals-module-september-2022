import re

usernames = re.split(r"[ /\\(),]+", input())
consecutive_usernames = []
all_consecutive_usernames = []

for username in usernames:
    valid_username = re.search(r"^[A-Za-z]\w{2,24}$", username)

    if valid_username:
        consecutive_usernames.append(valid_username.group())
        if len(consecutive_usernames) == 2:
            all_consecutive_usernames.append(consecutive_usernames[:])
            consecutive_usernames.pop(0)

longest_strings = "\n".join(max(all_consecutive_usernames, key=lambda strings: len("".join(strings))))

print(longest_strings)
