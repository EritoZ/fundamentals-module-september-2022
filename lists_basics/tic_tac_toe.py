first_player_moves = []
second_player_moves = []
first_player_won = False
second_player_won = False

for row in range(3):
    tic_tac_toe = input().split(" ")
    counter1 = 0
    counter2 = 0
    for i, number in enumerate(tic_tac_toe):
        if number == "1":
            first_player_moves.append(f"{i} - {row}")
            counter1 += 1
        elif number == "2":
            second_player_moves.append(f"{i} - {row}")
            counter2 += 1

    if counter1 == 3:
        first_player_won = True
        break
    elif counter2 == 3:
        second_player_won = True
        break

if (first_player_moves == ["0 - 0", "1 - 1", "2 - 2"]
        or first_player_moves == ["2 - 0", "1 - 1", "0 - 2"]
        or first_player_moves == ["0 - 0", "0 - 1", "0 - 2"]
        or first_player_moves == ["1 - 0", "1 - 1", "1 - 2"]
        or first_player_moves == ["2 - 0", "2 - 1", "2 - 2"]):
    first_player_won = True
elif (second_player_moves == ["0 - 0", "1 - 1", "2 - 2"]
      or second_player_moves == ["2 - 0", "1 - 1", "0 - 2"]
      or second_player_moves == ["0 - 0", "0 - 1", "0 - 2"]
      or second_player_moves == ["1 - 0", "1 - 1", "1 - 2"]
      or second_player_moves == ["2 - 0", "2 - 1", "2 - 2"]):
    second_player_won = True

if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")
