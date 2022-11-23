concealed_message = input()

command = input()
while command != "Reveal":
    command = command.split(":|:")
    instruction = command[0]

    if instruction == "InsertSpace":
        index = int(command[1])

        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif instruction == "Reverse":
        substring = command[1]

        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print("error")

    elif instruction == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
