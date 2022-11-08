import sys

contests = {}
submissions = {}

command = input()
while command != "end of contests":
    contest, password_contest = command.split(":")

    contests[contest] = password_contest

    command = input()

command = input()
while command != "end of submissions":
    command = command.split("=>")
    contest, password, username, points = command[0], command[1], command[2], int(command[3])

    if contest in contests and contests[contest] == password:
        if username in submissions and contest in submissions[username]:
            if points > submissions[username][contest]:
                submissions[username][contest] = points
        else:
            if username not in submissions:
                submissions[username] = {}
            submissions[username][contest] = points

    command = input()

most_points = -sys.maxsize
user_most_points = ""

for user in submissions:
    if sum(submissions[user].values()) > most_points:
        most_points = sum(submissions[user].values())
        user_most_points = user

for user in submissions:
    submissions[user] = dict(sorted(submissions[user].items(), key=lambda x: x[1], reverse=True))

submissions = dict(sorted(submissions.items()))

print(f"Best candidate is {user_most_points} with total {most_points} points.")
print("Ranking:")
for name in submissions:
    print(name)
    for contest in submissions[name]:
        points = submissions[name][contest]
        print(f"#  {contest} -> {points}")
