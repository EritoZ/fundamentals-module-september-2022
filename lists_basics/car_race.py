import math

sequence_of_numbers = input().split(" ")
left_car = 0
right_car = 0

for number in range(math.floor(len(sequence_of_numbers) / 2)):
    if sequence_of_numbers[number] == "0":
        left_car *= 0.8
    else:
        left_car += int(sequence_of_numbers[number])

for number in range(len(sequence_of_numbers) - 1, math.floor(len(sequence_of_numbers) / 2), -1):
    if sequence_of_numbers[number] == "0":
        right_car *= 0.8
    else:
        right_car += int(sequence_of_numbers[number])

if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
elif left_car > right_car:
    print(f"The winner is right with total time: {right_car:.1f}")
