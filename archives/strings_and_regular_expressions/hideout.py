import re

string_map = input()

while True:
    clue = input().split()
    mark, count = clue[0], int(clue[1])

    hideout = re.search(fr"\{mark}{{{count},}}", string_map)

    if hideout:
        hideout = hideout.group()
        print(f"Hideout found at index {string_map.index(hideout)} and it is with size {len(hideout)}!")
        break
