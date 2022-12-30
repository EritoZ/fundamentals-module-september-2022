def check_right(spot_index, row_index, been_there_list, the_matrix):
    if spot_index + 1 in range(len(the_matrix[row_index])) and \
            the_matrix[row_index][spot_index + 1] == "." and [row_index, spot_index + 1] not in been_there_list:
        return True

    return False


def check_up(spot_index, row_index, been_there_list, the_matrix):
    if row_index - 1 in range(len(the_matrix)) and \
            the_matrix[row_index - 1][spot_index] == "." and [row_index - 1, spot_index] not in been_there_list:
        return True

    return False


def check_down(spot_index, row_index, been_there_list, the_matrix):
    if row_index + 1 in range(len(the_matrix)) and \
            the_matrix[row_index + 1][spot_index] == "." and [row_index + 1, spot_index] not in been_there_list:
        return True

    return False


def check_left(spot_index, row_index, been_there_list, the_matrix):
    if spot_index - 1 in range(len(the_matrix[row_index])) and \
            the_matrix[row_index][spot_index - 1] == "." and [row_index, spot_index - 1] not in been_there_list:
        return True

    return False


row_n = int(input())
matrix = [input().split() for row in range(row_n)]
past_indexes = []
all_counts = []
finished = False
count = 0

connected_dots_indexes = []
current_row = 0
spot_start = 0
spot_initial_start = {"start": False, "row": 0, "spot": 0}
while not finished:
    for spot in range(spot_start, len(matrix[current_row])):

        if matrix[current_row][spot] == "." and [current_row, spot] not in past_indexes:

            if not spot_initial_start["start"]:
                spot_initial_start["start"] = True
                spot_initial_start["row"] = current_row
                spot_initial_start["spot"] = spot

            if [current_row, spot] in connected_dots_indexes:
                connected_dots_indexes.remove([current_row, spot])

            past_indexes.append([current_row, spot])
            count += 1

            if check_up(spot, current_row, past_indexes, matrix):
                connected_dots_indexes.append([current_row - 1, spot])

            if check_down(spot, current_row, past_indexes, matrix):
                connected_dots_indexes.append([current_row + 1, spot])

            if check_left(spot, current_row, past_indexes, matrix):
                connected_dots_indexes.append([current_row, spot - 1])

            if not check_right(spot, current_row, past_indexes, matrix):

                if connected_dots_indexes:
                    current_row = connected_dots_indexes[0][0]
                    spot_start = connected_dots_indexes[0][1]
                else:
                    all_counts.append(count)
                    count = 0
                    current_row = spot_initial_start["row"]
                    spot_start = spot_initial_start["spot"]
                    spot_initial_start["start"] = False

                break

    else:
        if current_row + 1 == row_n:
            finished = True
        else:
            current_row += 1
            spot_start = 0

print(max(all_counts, default=0))
