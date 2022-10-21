events = input().split("|")
energy = 100
coins = 100
handled_events = True

for event in events:
    event = event.split("-")
    event_name_or_ingredient = event[0]
    number = int(event[1])

    if "rest" == event_name_or_ingredient:
        if energy < 100:
            energy += number
            diff = number
            if energy > 100:
                diff -= energy - 100
                energy = 100
            print(f"You gained {diff} energy.")
            print(f"Current energy: {energy}.")
        else:
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
    elif "order" == event_name_or_ingredient:
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_name_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_name_or_ingredient}.")
            handled_events = False
            break

if handled_events:
    print(f"""Day completed!
Coins: {coins}
Energy: {energy}""")
