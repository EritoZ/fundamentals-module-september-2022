def is_valid(username):
    if len(username) in range(3, 17):
        for character in username:
            if not (character.isalnum() or character in ["-", "_"]):
                break
        else:
            return True

    return False


names = input().split(", ")

for name in names:
    if is_valid(name):
        print(name)
