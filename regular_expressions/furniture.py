import re

pattern = r">>([A-Za-z]+)<<(\d+(?:\.\d+)?)!(\d+)"
command = input()
total_spent = 0
print("Bought furniture:")
while command != "Purchase":
    purchase_data = command

    stats = re.findall(pattern, purchase_data)

    if stats:
        furniture, cost, quantity = stats[0][0], float(stats[0][1]), int(stats[0][2])

        total_spent += cost * quantity

        print(furniture)

    command = input()

print(f"Total money spend: {total_spent:.2f}")
