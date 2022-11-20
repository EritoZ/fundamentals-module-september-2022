import re

demons = input().split(",")
demon_dictionary = {}

for demon in demons:
    demon = demon.strip()

    demon_health = sum(map(ord, re.findall(r"[^0-9+\-*/.]", demon)))
    demon_damage = sum(map(float, re.findall(r"-?\d+(?:\.\d+)?", demon)))

    arithmetic_symbols = re.findall(r"[*/]", demon)

    for symbol in arithmetic_symbols:
        if symbol == "*":
            demon_damage *= 2
        elif symbol == "/":
            demon_damage /= 2

    demon_dictionary[demon] = [demon_health, demon_damage]

# noinspection PyTypeChecker
demon_dictionary = dict(sorted(demon_dictionary.items()))

for demon in demon_dictionary:
    print(f"{demon} - {demon_dictionary[demon][0]} health, {demon_dictionary[demon][1]:.2f} damage")
