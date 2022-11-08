players = {}

command = input()
while command != "Season end":
    if " -> " in command:
        command = command.split(" -> ")
        player, position, skill = command[0], command[1], int(command[2])

        if player not in players:
            players[player] = {}

        if position not in players[player]:
            players[player][position] = skill
        else:
            if skill > players[player][position]:
                players[player][position] = skill

    elif " vs " in command:
        player1, player2 = command.split(" vs ")

        if player1 in players and player2 in players:
            player1_position_skills = []
            player2_position_skills = []
            for position in players[player1]:
                if position in players[player2]:
                    player1_position_skills.append(players[player1][position])
                    player2_position_skills.append(players[player2][position])

            if sum(player1_position_skills) > sum(player2_position_skills):
                players.pop(player2)
            elif sum(player1_position_skills) < sum(player2_position_skills):
                players.pop(player1)

    command = input()

players = dict(sorted(players.items(), key=lambda player: player[0]))

players = dict(sorted(players.items(), key=lambda player: sum(player[1].values()), reverse=True))

for player in players:
    players[player] = dict(sorted(players[player].items(), key=lambda position: position[0]))
    players[player] = dict(sorted(players[player].items(), key=lambda position: position[1], reverse=True))

for player in players:
    print(f"{player}: {sum(players[player].values())} skill")
    for position in players[player]:
        print(f"- {position} <::> {players[player][position]}")
