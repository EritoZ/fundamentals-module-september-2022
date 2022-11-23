groceries = input().split("!")

command = input()
while command != "Go Shopping!":
    command = command.split(" ")

    if "Urgent" in command:
        item = command[1]
        if item not in groceries:
            new_lst = []
            for i in range(len(groceries)):
                if i == 0:
                    new_lst.append(item)
                new_lst.append(groceries[i])
            groceries = new_lst
    elif "Unnecessary" in command:
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif "Correct" in command:
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            for i, item in enumerate(groceries):
                if item == old_item:
                    groceries[i] = new_item
    else:
        item = command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    command = input()

print(", ".join(groceries))