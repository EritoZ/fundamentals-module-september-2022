def travel(fuel, distance):
    fuel -= distance

    return fuel


def enemy(enemy_armour, ammo):
    ammo -= enemy_armour

    return ammo


def repair(fuel, ammo, value):
    fuel += value
    ammo += 2 * value

    return fuel, ammo


travel_route = input().split("||")
initial_fuel = int(input())
initial_ammunition = int(input())

for event in travel_route:
    event = event.split()
    action = event[0]

    if action == "Travel":
        travel_distance = int(event[1])
        if initial_fuel >= travel_distance:
            initial_fuel = travel(initial_fuel, travel_distance)
            print(f"The spaceship travelled {travel_distance} light-years.")
        else:
            print("Mission failed.")
            break
    elif action == "Enemy":
        enemy_health = int(event[1])
        if initial_ammunition >= enemy_health:
            initial_ammunition = enemy(enemy_health, initial_ammunition)
            print(f"An enemy with {enemy_health} armour is defeated.")
        else:
            if initial_fuel < enemy_health * 2:
                print("Mission failed.")
                break
            else:
                initial_fuel -= enemy_health * 2
                print(f"An enemy with {enemy_health} armour is outmaneuvered.")
    elif action == "Repair":
        fuel_and_ammo_added = int(event[1])
        initial_fuel, initial_ammunition = repair(initial_fuel, initial_ammunition, fuel_and_ammo_added)
        print(f"""Ammunitions added: {fuel_and_ammo_added * 2}.
Fuel added: {fuel_and_ammo_added}.""")
    else:
        print("You have reached Titan, all passengers are safe.")
        break
