command = input()

while command != "end":
    word = command

    print(f"{word} = {word[::-1]}")

    command = input()
