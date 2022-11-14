keys = list(map(int, input().split()))

command = input()
while command != "find":
    a_string = command
    message = []

    index = 0
    for character in a_string:
        message.append(chr(ord(character) - keys[index]))
        index += 1

        if index == len(keys):
            index -= len(keys)

    formed_message = "".join(message)
    start_index_type = 0
    end_index_type = 0
    start_index_coordinates = 0
    end_index_coordinates = 0

    for i, symbol in enumerate(formed_message):
        if symbol == "&":
            if start_index_type:
                end_index_type = i
                continue
            start_index_type = i + 1
        elif symbol == "<":
            start_index_coordinates = i + 1
        elif symbol == ">":
            end_index_coordinates = i

    print(f"Found {formed_message[start_index_type:end_index_type]} at "
          f"{formed_message[start_index_coordinates:end_index_coordinates]}")

    command = input()
