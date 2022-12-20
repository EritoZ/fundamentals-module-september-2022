def check_right(spot_index, row_index, been_there_list, the_maze):
    if spot_index + 1 in range(len(the_maze[row_index])) and \
            the_maze[row_index][spot_index + 1] == " " and [row_index, spot_index + 1] not in been_there_list:
        return True
    else:
        return False


def check_up(spot_index, row_index, been_there_list, the_maze):
    if row_index - 1 in range(len(the_maze)) and \
            the_maze[row_index - 1][spot_index] == " " and [row_index - 1, spot_index] not in been_there_list:
        return True
    else:
        return False


def check_down(spot_index, row_index, been_there_list, the_maze):
    if row_index + 1 in range(len(the_maze)) and \
            the_maze[row_index + 1][spot_index] == " " and [row_index + 1, spot_index] not in been_there_list:
        return True
    else:
        return False


def check_left(spot_index, row_index, been_there_list, the_maze):
    if spot_index - 1 in range(len(the_maze[row_index])) and \
            the_maze[row_index][spot_index - 1] == " " and [row_index, spot_index - 1] not in been_there_list:
        return True
    else:
        return False


def at_the_finish_line(spot_index, row_index, exit_indexes_list, the_maze):
    if ((spot_index == 0 or
            spot_index == len(the_maze[row_index]) - 1 or
            row_index == 0 or
            row_index == len(the_maze) - 1) and
            [row_index, spot_index] not in exit_indexes_list
    ):
        return True
    else:
        return False


row_n = int(input())
kate_location = {"row": 0, "kate": 0}
maze = []
been_there_indexes = []
routes = []
exit_indexes = []
moves = 0
finished = False
no_out = True
reverse = False

for i in range(row_n):
    row = input()
    maze.append(row)
    if "k" in row:
        kate_location["row"] = i
        kate_location["kate"] = row.index("k")

current_row_index = kate_location["row"]
start = kate_location["kate"]
while not finished:

    if reverse:
        current_row = -1
        direction = -1
    else:
        current_row = len(maze[current_row_index])
        direction = 1

    for spot in range(start, current_row, direction):

        if [current_row_index, spot] not in been_there_indexes:
            been_there_indexes.append([current_row_index, spot])
            moves += 1

        if at_the_finish_line(spot, current_row_index, exit_indexes, maze):
            routes.append(moves)
            exit_indexes.append([current_row_index, spot])
            moves = 1
            current_row_index = kate_location["row"]
            start = kate_location["kate"]
            no_out = False
            reverse = False
            break

        if check_right(spot, current_row_index, been_there_indexes, maze):
            reverse = False

        elif check_up(spot, current_row_index, been_there_indexes, maze):
            current_row_index -= 1
            start = spot
            reverse = False
            break

        elif check_down(spot, current_row_index, been_there_indexes, maze):
            current_row_index += 1
            start = spot
            reverse = False
            break

        elif check_left(spot, current_row_index, been_there_indexes, maze):
            if not reverse:
                reverse = True
                break

        else:
            finished = True
            break

if not no_out:
    print(f"Kate got out in {max(routes)} moves")
else:
    print("Kate cannot get out")
