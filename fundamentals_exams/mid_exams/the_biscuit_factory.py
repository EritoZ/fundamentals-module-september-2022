import math

biscuits_per_day = int(input())
workers = int(input())
competing_factory_total = int(input())
biscuits_total = 0

for day in range(1, 31):
    if day % 3 == 0:
        biscuits_total += math.floor(biscuits_per_day * 0.75 * workers)
        continue

    biscuits_total += biscuits_per_day * workers


print(f"You have produced {biscuits_total} biscuits for the past month.")
percentage_biscuits = biscuits_total / competing_factory_total * 100
if percentage_biscuits > 100:
    print(f"You produce {abs(100 - percentage_biscuits):.2f} percent more biscuits.")
else:
    print(f"You produce {100 - percentage_biscuits:.2f} percent less biscuits.")
