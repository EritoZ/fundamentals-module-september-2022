import re

text = input()
calories = 0
food_pattern = r"(#|\|)([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

food_information = re.findall(food_pattern, text)

for food in food_information:
    calories += int(food[-1])

days = calories // 2000

print(f"You have food to last you for: {days} days!")
for food in food_information:
    print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}")
