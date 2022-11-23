def fire(enemy_ship, index, damage):
    enemy_ship[index] -= damage

    return enemy_ship


def defend(ally_ship, outcome, start_index, end_index, damage):
    for section in range(start_index, end_index + 1):
        ally_ship[section] -= damage
        if ally_ship[section] <= 0:
            outcome = True
            break

    return ally_ship, outcome


def repair(ally_ship, index, health):
    if ally_ship[index] + health > maximum_health_section:
        ally_ship[index] = maximum_health_section
    else:
        ally_ship[index] += health

    return ally_ship


def status(ally_ship):
    counter = 0
    for section in ally_ship:
        if section < maximum_health_section * 0.2:
            counter += 1

    return counter


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health_section = int(input())
you_won = False
you_lost = False

command = input()
while command != "Retire":
    command = command.split()
    function = command[0]

    if function == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(warship)):
            warship = fire(warship, index, damage)
            if warship[index] <= 0:
                you_won = True
                break
    elif function == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            pirate_ship, you_lost = defend(pirate_ship, you_lost, start_index, end_index, damage)
            if you_lost:
                break
    elif function == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship)):
            pirate_ship = repair(pirate_ship, index, health)
    elif function == "Status":
        print(f"{status(pirate_ship)} sections need repair.")

    command = input()

if command == "Retire":
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
elif you_won:
    print("You won! The enemy ship has sunken.")
else:
    print("You lost! The pirate ship has sunken.")
