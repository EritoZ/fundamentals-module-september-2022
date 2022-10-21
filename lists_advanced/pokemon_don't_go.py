def increase_and_decrease(numbers, value_index):
    copy_integers = numbers.copy()
    for i, n in enumerate(copy_integers):
        if n <= value_index:
            copy_integers[i] += value_index
        elif n > value_index:
            copy_integers[i] -= value_index

    return copy_integers


integers = list(map(int, input().split(" ")))
total_score = 0

while integers:
    index = int(input())

    if index in range(len(integers)):
        value = integers.pop(index)
        total_score += value
        integers = increase_and_decrease(integers, value)

    elif index < 0:
        value = integers.pop(0)
        total_score += value
        integers.insert(0, integers[-1])
        integers = increase_and_decrease(integers, value)

    else:
        value = integers.pop(-1)
        total_score += value
        integers.append(integers[0])
        integers = increase_and_decrease(integers, value)

print(total_score)
