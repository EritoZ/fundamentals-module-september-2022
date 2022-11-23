price_no_tax = 0
price_tax = 0
tax = 0

command = input()
while True:
    if command == "special":
        if price_tax == 0:
            print("Invalid order!")
        break
    elif command == "regular":
        if price_tax == 0:
            print("Invalid order!")
        break
    price = float(command)

    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    elif price == 0:
        print("Invalid order!")
        command = input()
        continue

    price_tax += price + price * 0.2
    tax += price * 0.2
    price_no_tax += price

    command = input()

customer = command

if customer == "special":
    price_tax *= 0.90

if price_tax > 0:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {price_no_tax:.2f}$
Taxes: {tax:.2f}$
-----------
Total price: {price_tax:.2f}$
""")
