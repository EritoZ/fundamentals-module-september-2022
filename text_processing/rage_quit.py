baby_rage = input()
harder_baby_rage = []
current_string = ""
digit = ""

for i, symbol in enumerate(baby_rage):
    if not symbol.isdigit():
        current_string += symbol.upper()
    else:
        digit += symbol
        if i == len(baby_rage) - 1 or not baby_rage[i + 1].isdigit():
            [harder_baby_rage.append(s) for s in current_string * int(digit)]
            current_string = ""
            digit = ""

print(f"Unique symbols used: {len(set(harder_baby_rage))}")
print("".join(harder_baby_rage))
