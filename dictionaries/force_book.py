def add(side, user, book):
    all_dudes = [dude for dudes in book.values() for dude in dudes]
    if side not in book and user not in all_dudes:
        book[side] = [user]
    elif user not in all_dudes:
        book[side].append(user)

    return book


def change(user, side, book):
    all_dudes = [dude for dudes in book.values() for dude in dudes]
    if side not in book:
        book[side] = []

    if user not in all_dudes:
        book[side].append(user)
    else:
        [users.remove(user) for side, users in book.items() if user in users]
        book[side].append(user)

    return book


force_book = {}

command = input()
while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        force_book = add(force_side, force_user, force_book)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        force_book = change(force_user, force_side, force_book)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for jedi in force_book[side]:
            print(f"! {jedi}")
