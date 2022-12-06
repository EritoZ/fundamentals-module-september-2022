guest_meals = {}
disliked_meals = 0

command = input()
while command != "Stop":
    command = command.split("-")
    current_command = command[0]
    guest = command[1]
    meal = command[2]

    if current_command == "Like":

        if guest not in guest_meals:
            guest_meals[guest] = [meal]

        if meal not in guest_meals[guest]:
            guest_meals[guest].append(meal)

    elif current_command == "Dislike":

        if guest in guest_meals:
            if meal in guest_meals[guest]:
                guest_meals[guest].remove(meal)

                print(f"{guest} doesn't like the {meal}.")
                disliked_meals += 1

            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

    command = input()

for guest in guest_meals:
    print(f"{guest}: {', '.join(guest_meals[guest])}")

print(f"Unliked meals: {disliked_meals}")
