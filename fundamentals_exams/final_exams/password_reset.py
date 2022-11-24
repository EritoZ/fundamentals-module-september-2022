a_string = input()

command = input()
while command != "Done":
    command = command.split()
    current_command = command[0]

    if current_command == "TakeOdd":

        a_string = "".join([a_string[letter] for letter in range(1, len(a_string), 2)])
        print(a_string)

    elif current_command == "Cut":
        index = int(command[1])
        length = int(command[2])

        a_string = a_string.replace(a_string[index:index + length], "", 1)
        print(a_string)

    elif current_command == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in a_string:
            a_string = a_string.replace(substring, substitute)
            print(a_string)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {a_string}")
