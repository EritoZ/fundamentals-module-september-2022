rooms = int(input())
extra_chairs = 0
game_on = True

for room in range(1, rooms + 1):
    chairs_and_visitors = input().split(" ")
    chairs = chairs_and_visitors[0].count("X")
    visitors = int(chairs_and_visitors[1])

    if chairs < visitors:
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False
    else:
        extra_chairs += chairs - visitors

if game_on:
    print(f"Game On, {extra_chairs} free chairs left")
