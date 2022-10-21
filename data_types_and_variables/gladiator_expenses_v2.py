lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

broken_helmet = lost_fights // 2
broken_sword = lost_fights // 3
broken_shield = lost_fights // 6
broken_armour = broken_shield // 2

total_sum = broken_helmet * helmet_price + broken_sword * sword_price + broken_shield * shield_price + \
            broken_armour * armour_price

print(f"Gladiator expenses: {total_sum:.2f} aureus")