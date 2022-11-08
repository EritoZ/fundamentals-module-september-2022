products_quantities = input().split()
products_to_check = input().split()
dictionary = {products_quantities[thing]: products_quantities[thing + 1] for thing in range(0, len(products_quantities), 2)}

for product in products_to_check:
    if product in dictionary.keys():
        print(f"We have {dictionary[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
