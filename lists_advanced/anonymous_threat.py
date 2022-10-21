def merge(start_index, end_index):
    copy_sequence_elements = sequence_elements.copy()
    counter = start_index
    while counter < end_index:
        copy_sequence_elements[start_index] += copy_sequence_elements.pop(start_index + 1)
        counter += 1

    return copy_sequence_elements


def divide(index, partition):
    copy_sequence_elements = sequence_elements.copy()
    if len(sequence_elements[index]) % partition == 0:
        ind = index
        copy_sequence_elements.pop(index)
        for i, el in enumerate(sequence_elements[index]):
            if i == 0:
                copy_sequence_elements.insert(ind, el)
                continue
            if len(copy_sequence_elements[ind]) % (len(sequence_elements[index]) / partition) == 0:
                ind += 1
                copy_sequence_elements.insert(ind, el)
                continue

            copy_sequence_elements[ind] += el
    else:
        ind = index
        copy_sequence_elements.pop(index)
        for i, el in enumerate(sequence_elements[index]):
            if i == 0:
                copy_sequence_elements.insert(ind, el)
                continue
            if len(copy_sequence_elements[ind]) == len(sequence_elements[index]) // partition and ind != partition - 1:
                ind += 1
                copy_sequence_elements.insert(ind, el)
                continue

            copy_sequence_elements[ind] += el

    return copy_sequence_elements


sequence_elements = input().split(" ")

command = input()
while command != "3:1":
    command = command.split(" ")
    function = command[0]
    index = int(command[1])
    index_or_partition = int(command[2])

    if function == "merge":
        if (index in range(len(sequence_elements))
            and index_or_partition in range(len(sequence_elements))
        ):
            sequence_elements = merge(index, index_or_partition)

        elif ((index in range(len(sequence_elements))
              or (index_or_partition in range(len(sequence_elements))))
        ):
            if index < 0:
                index = 0

            if index_or_partition >= len(sequence_elements):
                index_or_partition = len(sequence_elements) - 1

            sequence_elements = merge(index, index_or_partition)
        else:
            if index < 0 and index_or_partition >= len(sequence_elements):
                index = 0
                index_or_partition = len(sequence_elements) - 1
            elif index >= len(sequence_elements):
                index = len(sequence_elements) - 2
                index_or_partition = len(sequence_elements) - 1
            elif index < 0:
                index = 0
                index_or_partition = 1

            sequence_elements = merge(index, index_or_partition)

    elif function == "divide" and len(sequence_elements[index]) >= index_or_partition:
        sequence_elements = divide(index, index_or_partition)

    command = input()

print(" ".join(sequence_elements))
