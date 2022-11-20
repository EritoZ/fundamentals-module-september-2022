import re

race_participants = input().split(", ")
participants_results = {}

command = input()
while command != "end of race":
    data = command

    name = "".join(re.findall(r"[A-Za-z]", data))
    ran_distance = sum(map(int, re.findall(r"\d", data)))

    if name in race_participants:
        if name not in participants_results:
            participants_results[name] = 0
        participants_results[name] += ran_distance

    command = input()

participants_results = sorted(participants_results.items(), key=lambda participant: participant[1], reverse=True)

print(f"""1st place: {participants_results[0][0]}
2nd place: {participants_results[1][0]}
3rd place: {participants_results[2][0]}""")
