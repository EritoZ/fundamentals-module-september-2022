sequence_of_numbers = input().split(" ")
strings = [*input()]
message = ""

for numbers in sequence_of_numbers:
    index = 0
    for number in numbers:
        index += int(number)
        if index >= len(strings):
            index -= len(strings)

    message += strings.pop(index)

print(message)
