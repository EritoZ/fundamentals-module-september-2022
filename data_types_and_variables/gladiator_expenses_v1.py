lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armour = 0

for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0:
        broken_helmet += 1
    if lost_fight % 3 == 0:
        broken_sword += 1
        if lost_fight % 2 == 0:
            broken_shield += 1
            if broken_shield % 2 == 0:
                broken_armour += 1

total_sum = broken_helmet * helmet_price + broken_sword * sword_price + broken_shield * shield_price + \
            broken_armour * armour_price

print(f"Gladiator expenses: {total_sum:.2f} aureus")