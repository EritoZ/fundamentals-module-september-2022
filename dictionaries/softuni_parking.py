def register(user, plate_number):
    if user not in users:
        users[user] = plate_number
        return f"{user} registered {plate_number} successfully"
    else:
        return f"ERROR: already registered with plate number {plate_number}"


def unregister(user):
    if user in users:
        users.pop(user)
        return f"{user} unregistered successfully"
    else:
        return f"ERROR: user {user} not found"


number = int(input())
users = {}

for _ in range(number):
    data = input().split()
    command, username = data[0], data[1]

    if command == "register":
        license_plate_number = data[2]
        print(register(username, license_plate_number))

    elif command == "unregister":
        print(unregister(username))

[print(f"{user} => {users[user]}") for user in users]
