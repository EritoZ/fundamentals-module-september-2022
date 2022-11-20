import re

pattern = r"%([A-Z][a-z]+)%.*?<(\w+)>.*?\|(\d+)\|.*?(\d+(?:\.\d+)?)\$"
total_amount = 0

command = input()
while command != "end of shift":
    order = re.search(pattern, command)

    if order:
        customer, product, count, price = order.group(1), order.group(2), int(order.group(3)), float(order.group(4))

        total_price = count * price

        print(f"{customer}: {product} - {total_price:.2f}")
        total_amount += total_price

    command = input()

print(f"Total income: {total_amount:.2f}")
