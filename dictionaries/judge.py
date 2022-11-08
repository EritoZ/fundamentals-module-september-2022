user_submissions = {}
user_max_points = {}

command = input()
while command != "no more time":
    command = command.split(" -> ")
    username, contest, points = command[0], command[1], int(command[2])

    if contest in user_submissions and username in user_submissions[contest]:
        if user_submissions[contest][username] < points:
            user_max_points[username] += points - user_max_points[username]
            user_submissions[contest][username] = points
    else:
        if contest not in user_submissions:
            user_submissions[contest] = {}
        user_submissions[contest][username] = points

        if username not in user_max_points:
            user_max_points[username] = 0
        user_max_points[username] += points

    command = input()

for contest in user_submissions:
    user_submissions[contest] = dict(sorted(user_submissions[contest].items(), key=lambda user: user[0]))
    user_submissions[contest] = dict(sorted(user_submissions[contest].items(), key=lambda user: user[1], reverse=True))

# noinspection PyTypeChecker
user_max_points = dict(sorted(user_max_points.items(), key=lambda user: user[0]))

# noinspection PyTypeChecker
user_max_points = dict(sorted(user_max_points.items(), key=lambda user: user[1], reverse=True))

for contest in user_submissions:
    print(f"{contest}: {len(user_submissions[contest])} participants")
    for i, user in enumerate(user_submissions[contest], 1):
        print(f"{i}. {user} <::> {user_submissions[contest][user]}")

print("Individual standings:")
for i, user in enumerate(user_max_points, 1):
    print(f"{i}. {user} -> {user_max_points[user]}")
