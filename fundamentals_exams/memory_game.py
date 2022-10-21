def new_list(elements):
    new_sequence = []
    for i in range(len(elements)):
        if i == len(elements) // 2:
            new_sequence.append(f"-{moves}a")
            new_sequence.append(f"-{moves}a")

        new_sequence += sequence_elements[i]

    return new_sequence


sequence_elements = input().split(" ")
moves = 0

command = input()
while command != "end":
    indexes_elements = command.split(" ")
    moves += 1
    index1 = int(indexes_elements[0])
    index2 = int(indexes_elements[1])

    if (
        index1 not in range(len(sequence_elements))
        or index2 not in range(len(sequence_elements))
        or index1 == index2
    ):
        sequence_elements = new_list(sequence_elements)
        print("Invalid input! Adding additional elements to the board")
    elif sequence_elements[index1] == sequence_elements[index2]:
        popped = sequence_elements.pop(index1)
        if index2 == 0:
            sequence_elements.pop(index2)
        else:
            sequence_elements.pop(index2 - 1)
        print(f"Congrats! You have found matching elements - {popped}!")
    else:
        print("Try again!")

    if len(sequence_elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    command = input()

if len(sequence_elements) > 0:
    print(f"""Sorry you lose :(
{" ".join(sequence_elements)}
""")
