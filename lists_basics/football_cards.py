cards = input()
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
eliminated_a = []
eliminated_b = []
terminated = False

cards = cards.split(" ")

for card in cards:
    if "A" in card:
        for number in range(11, 0, -1):
            if str(number) in card and number not in eliminated_a:
                team_a.remove(number)
                eliminated_a.append(number)
                break
    elif "B" in card:
        for number in range(11, 0, -1):
            if str(number) in card and number not in eliminated_b:
                team_b.remove(number)
                eliminated_b.append(number)
                break
    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated:
    print("Game was terminated")
