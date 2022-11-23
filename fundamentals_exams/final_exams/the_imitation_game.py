encrypted_message = input()

command = input()
while command != "Decode":
    command = command.split("|")
    instruction = command[0]

    if instruction == "Move":
        n_letters = int(command[1])
        moved_letters = encrypted_message[:n_letters]

        encrypted_message = encrypted_message[n_letters:]
        encrypted_message += moved_letters

    elif instruction == "Insert":
        index, value = int(command[1]), command[2]

        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif instruction == "ChangeAll":
        substring, replacement = command[1], command[2]

        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
