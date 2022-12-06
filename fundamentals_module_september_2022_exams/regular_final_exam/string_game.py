a_string = input()

command = input()
while command != "Done":
    command = command.split()
    current_command = command[0]

    if current_command == "Change":
        char = command[1]
        replacement = command[2]

        a_string = a_string.replace(char, replacement)

        print(a_string)

    elif current_command == "Includes":
        substring_includes = command[1]

        if substring_includes in a_string:
            print(True)
        else:
            print(False)

    elif current_command == "End":
        substring_end = command[1]

        if a_string[len(a_string) - len(substring_end):] == substring_end:
            print(True)
        else:
            print(False)

    elif current_command == "Uppercase":

        a_string = a_string.upper()

        print(a_string)

    elif current_command == "FindIndex":
        char_find_index = command[1]

        print(a_string.index(char_find_index))

    elif current_command == "Cut":
        start_index = int(command[1])
        count = int(command[2])

        cut_chars = a_string[start_index:start_index + count]

        a_string = a_string[:start_index] \
                   + a_string[start_index + count:]

        print(cut_chars)

    command = input()
