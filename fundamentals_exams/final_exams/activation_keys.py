activation_key = input()

command = input()
while command != "Generate":
    command = command.split(">>>")
    current_command = command[0]

    if current_command == "Contains":
        substring = command[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current_command == "Flip":
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        if upper_or_lower == "Upper":
            activation_key = activation_key[:start_index] + \
                             activation_key[start_index:end_index].upper() + \
                             activation_key[end_index:]

        elif upper_or_lower == "Lower":
            activation_key = activation_key[:start_index] + \
                             activation_key[start_index:end_index].lower() + \
                             activation_key[end_index:]
            
        print(activation_key)
        
    elif current_command == "Slice":
        index_start = int(command[1])
        index_end = int(command[2])

        activation_key = activation_key.replace(activation_key[index_start:index_end], "", 1)
        
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
