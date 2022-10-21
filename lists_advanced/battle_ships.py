rows = int(input())
field_rows = []
dead = 0

for row in range(rows):
    field_rows.append(list(map(int, input().split())))

attacks = input().split()

for y, row in enumerate(field_rows):
    for x, spot in enumerate(row):
        if spot > 0 and f"{y}-{x}" in attacks:
            row[x] -= attacks.count(f"{y}-{x}")
            if row[x] <= 0:
                dead += 1

print(dead)
