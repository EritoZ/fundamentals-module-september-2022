import re

pattern = r"@([A-Za-z]+)[^@\-!:>]*:\d+[^@\-!:>]*!(A|D)![^@\-!:>]*\->\d+"
attacked = []
destroyed = []

messages_count = int(input())
for _ in range(messages_count):
    message = input()

    count_letters = len(re.findall(r"[starSTAR]", message))
    message = "".join(map(lambda symbol: chr(ord(symbol) - count_letters), message))

    decrypted_message = re.search(pattern, message)

    if decrypted_message:
        planet = decrypted_message.group(1)
        attack_type = decrypted_message.group(2)

        if attack_type == "A":
            attacked.append(planet)
        elif attack_type == "D":
            destroyed.append(planet)

attacked = sorted(attacked)
destroyed = sorted(destroyed)

print(f"Attacked planets: {len(attacked)}")
for planet in attacked:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed)}")
for planet in destroyed:
    print(f"-> {planet}")
