import sys

integers = input()
numbers_to_remove = int(input())

integers = integers.split(" ")

for i in range(numbers_to_remove):
    smallest_number = sys.maxsize
    for number in integers:
        if int(number) < smallest_number:
            smallest_number = int(number)

    integers.remove(str(smallest_number))

print(", ".join(integers))
