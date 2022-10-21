def order_price(product, quantity):
    if product == "coffee":
        product = 1.50
    elif product == "water":
        product = 1.00
    elif product == "coke":
        product = 1.40
    elif product == "snacks":
        product = 2.00
    return product * quantity


item = input()
quantity = int(input())

price = order_price(item, quantity)
print(f"{price:.2f}")
