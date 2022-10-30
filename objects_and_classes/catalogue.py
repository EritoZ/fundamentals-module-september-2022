class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return list(filter(lambda product: product[0] == first_letter, self.products))

    def __repr__(self):
        new_row = "\n"
        return f"Items in the {self.name} catalogue:\n{new_row.join(sorted(self.products))}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
catalogue_fruits = Catalogue("Fruits")
catalogue_fruits.add_product("Banana")
catalogue_fruits.add_product("Ananas")
print(catalogue_fruits)
