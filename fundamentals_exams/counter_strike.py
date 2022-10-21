energy = int(input())
won_battles = 0
no_energy = False

command = input()
while command != "End of battle":
    distance = int(command)

    if energy >= distance:
        energy -= distance
        won_battles += 1
    else:
        no_energy = True
        break

    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

if no_energy:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
