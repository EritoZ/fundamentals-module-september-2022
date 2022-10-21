from decimal import Decimal

food_quantity = Decimal(input())
hay_quantity = Decimal(input())
cover_quantity = Decimal(input())
pig_weight = Decimal(input())
not_enough = False

for day in range(1, 31):
    food_quantity -= Decimal("0.3")

    if day % 2 == 0:
        hay_quantity -= food_quantity * Decimal("0.05")

    if day % 3 == 0:
        cover_quantity -= pig_weight * Decimal("0.333")

    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        not_enough = True
        break

if not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f},"
          f" Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
