rows = int(input())
previous_coordinates = []
found_object = False
no_exit = False
found_kate = False
first_row_exit = False
left_or_right_exit = False
longest_route = []
moves = 0
wall_counter_for_row = 0

for row in range(1, rows + 1):
    maze_row = input()
    coordinates = []
    for location, object in enumerate(maze_row, 1):
        if found_object and (object == " " or object == "k"):
            if object == "k":
                found_kate = True
            if location == 1 or location == len(maze_row):
                left_or_right_exit = True
            if maze_row[location - 1] == " " or maze_row[location - 1] == "k" or location in previous_coordinates:
                coordinates.append(location)
                moves += 1
                continue
            else:
                if object == "k" and (location != 1 or location != len(maze_row)):
                    no_exit = True
                    break
                found_object = False
                moves = 0
                first_row_exit = False
                left_or_right_exit = False
        else:
            wall_counter_for_row += 1
            if wall_counter_for_row == len(maze_row) and found_kate and not first_row_exit and not left_or_right_exit:
                no_exit = True
                break
        if object == " " or object == "k":
            coordinates.append(location)
            found_object = True
            moves += 1
            if object == "k":
                found_kate = True
            if row == 1:
                first_row_exit = True
            if location == 1 or location == len(maze_row):
                left_or_right_exit = True

    if no_exit:
        break

    wall_counter_for_row = 0

    previous_coordinates = coordinates

longest_route.append(moves)
moves = max(longest_route)

if no_exit:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {moves} moves")
