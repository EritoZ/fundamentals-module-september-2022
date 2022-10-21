fire_cells = input().split("#")
water_amount = int(input())
effort = 0
fire_total = 0

print("Cells:")
for i, cell in enumerate(fire_cells):
    cell = cell.split(" = ")

    if "High" in cell:
        if 81 <= int(cell[1]) <= 125:
            if int(cell[1]) > water_amount:
                continue
        else:
            continue
    elif "Medium" in cell:
        if 51 <= int(cell[1]) <= 80:
            if int(cell[1]) > water_amount:
                continue
        else:
            continue
    else:
        if 1 <= int(cell[1]) <= 50:
            if int(cell[1]) > water_amount:
                continue
        else:
            continue

    water_amount -= int(cell[1])
    effort += int(cell[1]) * 0.25
    fire_total += int(cell[1])
    print(f"- {cell[1]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_total}")
