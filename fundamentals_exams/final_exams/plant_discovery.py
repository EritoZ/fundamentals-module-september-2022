plant_dict = {}
number = int(input())

for _ in range(number):
    plant_info = input().split("<->")
    plant, rarity = plant_info[0], plant_info[1]

    plant_dict[plant] = [rarity, []]

command = input()
while command != "Exhibition":
    data = command.split()
    command, plant = data[0], data[1]

    if "Rate" in command:
        rating = int(data[3])

        if plant in plant_dict:
            plant_dict[plant][1].append(rating)
        else:
            print("error")

    elif "Update" in command:
        new_rarity = data[3]

        if plant in plant_dict:
            plant_dict[plant][0] = new_rarity
        else:
            print("error")

    elif "Reset" in command:

        if plant in plant_dict:
            plant_dict[plant][1].clear()
        else:
            print("error")

    command = input()

print(f"Plants for the exhibition:")
for plant in plant_dict:
    if plant_dict[plant][1]:
        average_rating = sum(plant_dict[plant][1]) / len(plant_dict[plant][1])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plant_dict[plant][0]}; Rating: {average_rating:.2f}")
