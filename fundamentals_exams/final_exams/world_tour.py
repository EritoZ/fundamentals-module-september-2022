stops = input()

command = input()
while command != "Travel":
    data = command.split(":")
    command, start_index_or_string, end_index_or_string  = data[0], data[1], data[2]

    if command == "Add Stop":
        start_index_or_string = int(start_index_or_string)

        if start_index_or_string in range(len(stops)):
            stops = stops[:start_index_or_string] + end_index_or_string + stops[start_index_or_string:]

    elif command == "Remove Stop":
        start_index_or_string = int(start_index_or_string)
        end_index_or_string = int(end_index_or_string)

        if start_index_or_string in range(len(stops)) and end_index_or_string in range(len(stops)):
            stops = stops[:start_index_or_string] + stops[end_index_or_string + 1:]

    elif command == "Switch":

        stops = stops.replace(start_index_or_string, end_index_or_string)

    if stops:
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
