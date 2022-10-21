array = list(map(int, input().split(" ")))

command = input()
while command != "end":
    command = command.split(" ")
    if "swap" in command:
        index1 = int(command[1])
        index2 = int(command[2])
        new_list = []
        for i in range(len(array)):
            if i == index1:
                new_list.append(array[index2])
                continue
            elif i == index2:
                new_list.append(array[index1])
                continue
            new_list.append(array[i])
        array = new_list
    elif "multiply" in command:
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1] = array[index1] * array[index2]
    else:
        for i, number in enumerate(array):
            array[i] = int(number) - 1

    command = input()

print(", ".join(list(map(str, array))))
