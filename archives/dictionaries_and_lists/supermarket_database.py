class Products:

    def __init__(self):
        self.products = {}
        self.total_cost = 0

    def add_product(self, product, price, quantity):
        if product not in self.products:
            self.products[product] = {"price": 0, "quantity": 0, "total": 0}
        self.products[product]["price"] = price
        self.products[product]["quantity"] += quantity
        self.products[product]["total"] = price * self.products[product]["quantity"]

    def sum_costs(self):
        self.total_cost = sum([self.products[product]["total"] for product in self.products])

    def __repr__(self):
        output = ""
        for product in self.products:
            output += f"{product}: " \
                      f"${self.products[product]['price']:.2f} * {self.products[product]['quantity']} = " \
                      f"${self.products[product]['total']:.2f}\n"

        output += "-" * 30 + "\n"
        output += f"Grand Total: ${self.total_cost:.2f}"

        return output


products = Products()
command = input()
while command != "stocked":
    product_data = command.split()
    name, price_data, quantity_data = product_data[0], float(product_data[1]), int(product_data[2])

    products.add_product(name, price_data, quantity_data)

    command = input()

products.sum_costs()

print(products)
