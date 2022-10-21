gifts = input().split()
new_list = []

command = input()
while command != "No Money":
    command = command.split(" ")

    if command[0] == "OutOfStock":
        for i, gift in enumerate(gifts):
            if command[1] == gift:
                gifts[i] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) <= len(gifts) - 1:
            gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input()

for item in gifts:
    if item != "None":
        new_list.append(item)

print(" ".join(new_list))
