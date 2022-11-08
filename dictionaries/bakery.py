goodies = input().split()
bakery = {goodies[something]: int(goodies[something + 1]) for something in range(0, len(goodies), 2)}

print(bakery)
