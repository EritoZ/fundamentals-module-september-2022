rows = int(input())
dots_and_dashes_rows = []
dots_indexes = -1

for row in range(rows):
    dots_and_dashes_rows.append(input().split())

for y, row in enumerate(dots_and_dashes_rows):
    for x, symbol in enumerate(row):
        if symbol == ".":
            if row[x - 1] == "." or dots_and_dashes_rows[y - 1][x] in dots_and_dashes_rows:
                dots_and_dashes_rows.insert()
            dots_and_dashes_rows.append([x, y])
            dots_indexes += 1