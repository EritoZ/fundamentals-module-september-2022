items = input().split("|")
budget = float(input())
starting_budget = budget
profit = 0
bought_items_price = []

for item in items:
    item = item.split("->")
    type_item = item[0]
    price_item = float(item[1])

    if "Clothes" in item:
        if 0 <= price_item <= 50.00 and budget >= price_item:
            budget -= price_item
            bought_items_price.append(price_item)
        else:
            continue
    elif "Shoes" in item:
        if 0 <= price_item <= 35.00 and budget >= price_item:
            budget -= price_item
            bought_items_price.append(price_item)
        else:
            continue
    elif "Accessories" in item:
        if 0 <= price_item <= 20.50 and budget >= price_item:
            budget -= price_item
            bought_items_price.append(price_item)
        else:
            continue

for i, price in enumerate(bought_items_price):
    new_price = round(float(price) * 1.4, 2)
    bought_items_price[i] = f"{new_price:.2f}"
    budget += new_price

profit = abs(starting_budget - budget)

print(f"""{" ".join(bought_items_price)}
Profit: {profit:.2f}""")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
