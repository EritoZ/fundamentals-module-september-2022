wagons = int(input())

lst_wagons = wagons * [0]

command = input()
while command != "End":
    command = command.split(" ")
    order = command[0]

    if order == "add":
        people = int(command[1])
        lst_wagons[-1] += people
    elif order == "insert":
        index = int(command[1])
        people = int(command[2])
        lst_wagons[index] += people
    else:
        index = int(command[1])
        people = int(command[2])
        lst_wagons[index] -= people

    command = input()

print(lst_wagons)