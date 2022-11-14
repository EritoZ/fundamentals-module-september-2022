string_input = [*input()]
counter = 0

for i, character in enumerate(string_input):
    if character == ">":
        counter += int(string_input[i + 1])

    elif counter:
        string_input[i] = " "
        counter -= 1

print("".join(string_input).replace(" ", ""))
