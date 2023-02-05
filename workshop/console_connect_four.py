from collections import deque


def directions_search(row_len, col_len, board, current_spot, player_info):
    row_i, col_i = current_spot

    left = [board[row_i][i] for i in range(col_i, -1, -1)]

    left_up = [board[row_i - i][col_i - i] for i in range(4)
               if row_i - i in range(row_len) and col_i - i in range(col_len)]

    up = [board[i][col_i] for i in range(row_i, -1, -1)][:4]

    up_right = [board[row_i - i][col_i + i] for i in range(4)
                if row_i - i in range(row_len) and col_i + i in range(col_len)]

    right = [board[row_i][i] for i in range(col_i, col_len)][:4]

    down_right = [board[row_i + i][col_i + i] for i in range(4)
                  if row_i + i in range(row_len) and col_i + i in range(col_len)]

    down = [board[i][col_i] for i in range(row_i, row_len)][:4]

    down_left = [board[row_i + i][col_i - i] for i in range(4)
                 if row_i + i in range(row_len) and col_i - i in range(col_len)]

    return 4 * [player_info] in (
            left, left_up, up, up_right,
            right, down_right, down, down_left
    )


def check_if_won(player_moves_counter, rows_len, columns_len, board, current_spot, player_info):

    return player_moves_counter >= 4 and directions_search(rows_len, columns_len, board, current_spot, player_info)


rows, columns = 6, 7
board_matrix = [[0] * 7 for _ in range(6)]
spots_n = 6 * 7
players = deque(([1, 0], [2, 0]))
winner = False

[print(row) for row in board_matrix]
while spots_n and not winner:

    current_player = players[0][0]

    try:
        column_choice = int(input(f'Player {current_player}, please choose a column\n')) - 1

        for i in range(rows):
            if i == rows - 1 or board_matrix[i + 1][column_choice] != 0:

                if column_choice < 0:
                    raise IndexError

                board_matrix[i][column_choice] = current_player
                players[0][1] += 1
                spots_n -= 1

                if check_if_won(players[0][1], rows, columns, board_matrix, [i, column_choice], current_player):
                    print(f'Player {current_player} won!')
                    winner = True
                    break

                break
        else:
            print('Column is full. Try again.')
            continue

    except (IndexError, ValueError):
        print('Please, type a number from 1 to 7.\n')
        [print(row) for row in board_matrix]

        continue

    [print(row) for row in board_matrix]

    players.rotate()

if not spots_n:
    print('Draw. Board is full.')
