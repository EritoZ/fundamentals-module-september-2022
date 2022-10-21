def forward(positions, index, steps):
    index += steps
    positions.pop(index)

    return positions, index


def back(positions, index, steps):
    index -= steps
    positions.pop(index)

    return positions, index


def gift(positions, command_index, house_number):
    positions.insert(command_index, house_number)

    return positions


def swap(positions, house1, house2):
    index1 = positions.index(house1)
    index2 = positions.index(house2)
    positions[index1], positions[index2] = positions[index2], positions[index1]

    return positions


number_of_commands = int(input())
integers = list(map(int, input().split()))
position = 0

for i in range(number_of_commands):
    command = input().split()
    function = command[0]

    if function == "Forward":
        steps = int(command[1])
        if position + steps in range(len(integers)):
            integers, position = forward(integers, position, steps)
    elif function == "Back":
        steps = int(command[1])
        if position - steps in range(len(integers)):
            integers, position = back(integers, position, steps)
    elif function == "Gift":
        index_house = int(command[1])
        house_number = int(command[2])
        if index_house in range(len(integers)):
            integers = gift(integers, index_house, house_number)
            position = index_house
    elif function == "Swap":
        house1 = int(command[1])
        house2 = int(command[2])
        if house1 in integers and house2 in integers:
            integers = swap(integers, house1, house2)

print(f"Position: {position}")
print(", ".join(list(map(str, integers))))
