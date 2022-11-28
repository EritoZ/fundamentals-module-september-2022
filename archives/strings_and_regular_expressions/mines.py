import re

characters = input()

mines = re.finditer(r"<(.{2})>", characters)

for mine in mines:
    explosion_range = abs(ord(mine.group(1)[0]) - ord(mine.group(1)[1]))

    left_radius = mine.start() - explosion_range
    if left_radius < 0:
        left_radius = 0

    right_radius = mine.end() + explosion_range
    if right_radius > len(characters):
        right_radius = len(characters)

    characters = characters[:left_radius] \
                 + len(characters[left_radius:right_radius]) * "_" \
                 + characters[right_radius:]

print(characters)
