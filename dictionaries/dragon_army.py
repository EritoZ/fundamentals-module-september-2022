dragon_dictionary = {}

dragons_amount = int(input())

for dragon in range(dragons_amount):
    type, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45
    damage = int(damage)
    if health == "null":
        health = 250
    health = int(health)
    if armor == "null":
        armor = 10
    armor = int(armor)

    if type not in dragon_dictionary:
        dragon_dictionary[type] = {}

    dragon_dictionary[type][name] = [damage, health, armor]

for type in dragon_dictionary:
    dragon_dictionary[type] = dict(sorted(dragon_dictionary[type].items(), key=lambda dragon: dragon[0]))

    average_attack = sum([dragon_dictionary[type][dragon][0] for dragon in dragon_dictionary[type]]) \
                     / len(dragon_dictionary[type])
    average_health = sum([dragon_dictionary[type][dragon][1] for dragon in dragon_dictionary[type]]) \
                     / len(dragon_dictionary[type])
    average_defense = sum([dragon_dictionary[type][dragon][2] for dragon in dragon_dictionary[type]]) \
                      / len(dragon_dictionary[type])

    print(f"{type}::({average_attack:.2f}/{average_health:.2f}/{average_defense:.2f})")
    for dragon in dragon_dictionary[type]:
        print(f"-{dragon} -> damage: {dragon_dictionary[type][dragon][0]},"
              f" health: {dragon_dictionary[type][dragon][1]}, armor: {dragon_dictionary[type][dragon][2]}")
