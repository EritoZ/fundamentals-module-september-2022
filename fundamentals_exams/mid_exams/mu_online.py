def potion(current_health, number):
    if current_health + number > 100:
        healed_amount = 100 - current_health
        current_health = 100
    else:
        current_health += number
        healed_amount = number

    return current_health, healed_amount


def attack(current_health, number):
    current_health -= number

    return current_health


dungeon_rooms = input().split("|")
health = 100
bitcoins = 0
dead = False

for i, room in enumerate(dungeon_rooms, 1):
    room = room.split()
    command = room[0]
    action = int(room[1])

    if command == "potion":
        health, healed = potion(health, action)
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += action
        print(f"You found {action} bitcoins.")
    else:
        health = attack(health, action)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i}")
            break

if not dead:
    print(f"""You've made it!
Bitcoins: {bitcoins}
Health: {health}
""")
