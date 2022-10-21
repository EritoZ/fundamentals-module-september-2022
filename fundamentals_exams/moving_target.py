targets = list(map(int, input().split(" ")))

command = input()
while command != "End":
    command = command.split(" ")
    index = int(command[1])
    value = int(command[2])

    if "Shoot" in command:
        if index in range(len(targets)):
            targets[index] = targets[index] - value
            if targets[index] <= 0:
                targets.pop(index)
    elif "Add" in command:
        if index in range(len(targets)):
            new_lst = []
            for i in range(len(targets)):
                if i == index:
                    new_lst.append(value)
                new_lst.append(targets[i])
            targets = new_lst
        else:
            print("Invalid placement!")
    elif "Strike" in command:
        new_lst = []
        counter = 0
        for i in range(len(targets)):
            if index - value <= i <= index + value:
                counter += 1
                continue
            new_lst.append(targets[i])
        if counter < value * 2 + 1:
            print("Strike missed!")
        else:
            targets = new_lst

    command = input()

print("|".join(list(map(str, targets))))
