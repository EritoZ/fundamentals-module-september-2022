import re

user_logs = {}

command = input()
while command != "end":
    data = re.search(r"IP=(.+?) .+?user=(.+)", command)
    ip, user = data.group(1), data.group(2)

    if user not in user_logs:
        user_logs[user] = {}

    if ip not in user_logs[user]:
        user_logs[user][ip] = 0
    user_logs[user][ip] += 1

    command = input()

for user in dict(sorted(user_logs.items())):
    print(f"{user}:\n{', '.join([f'{ip} => {user_logs[user][ip]}' for ip in user_logs[user]])}.")
