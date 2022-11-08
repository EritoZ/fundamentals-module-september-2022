bakery = {}
command = input()
while command != "statistics":
    product, quantity = command.split(": ")
    if product not in bakery.keys():
        bakery[product] = 0
    bakery[product] += int(quantity)

    command = input()

print("Products in stock:")
for product, quantity in bakery.items():
    print(f"- {product}: {quantity}")

print(f"""Total Products: {len(bakery)}
Total Quantity: {sum(bakery.values())}""")
