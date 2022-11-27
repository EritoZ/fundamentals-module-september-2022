target_cities = {}

command = input()
while command != "Sail":
    command = command.split("||")
    city = command[0]

    if city not in target_cities:
        target_cities[city] = {"population": 0, "gold": 0}
    target_cities[city]["population"] += int(command[1])
    target_cities[city]["gold"] += int(command[2])

    command = input()

command = input()
while command != "End":
    command = command.split("=>")
    current_command = command[0]
    town = command[1]

    if current_command == "Plunder":
        people, gold_in_town = int(command[2]), int(command[3])

        target_cities[town]["population"] -= people
        target_cities[town]["gold"] -= gold_in_town

        print(f"{town} plundered! {gold_in_town} gold stolen, {people} citizens killed.")

        if target_cities[town]["population"] == 0 or target_cities[town]["gold"] == 0:
            del target_cities[town]
            print(f"{town} has been wiped off the map!")

    elif current_command == "Prosper":
        gold_increase = int(command[2])

        if gold_increase < 0:
            print("Gold added cannot be a negative number!")
        else:
            target_cities[town]["gold"] += gold_increase
            print(f"{gold_increase} gold added to the city treasury. "
                  f"{town} now has {target_cities[town]['gold']} gold.")

    command = input()

if target_cities:
    print(f"Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:")
    for left_city in target_cities:
        print(f"{left_city} -> Population: {target_cities[left_city]['population']} citizens, "
              f"Gold: {target_cities[left_city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
