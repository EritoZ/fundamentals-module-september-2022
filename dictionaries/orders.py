products = {}

command = input()
while command != "buy":
    command = command.split()
    name, price, quantity = command[0], float(command[1]), int(command[2])

    if name not in products:
        products[name] = [0.0, 0]
    products[name][0] = price
    products[name][1] += quantity

    command = input()

[print(f"{product} -> {products[product][0] * products[product][1]:.2f}") for product in products]
