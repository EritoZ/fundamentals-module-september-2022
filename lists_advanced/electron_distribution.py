electrons = int(input())
shells = []
counter = 0

while electrons > 0:
    counter += 1
    equation = 2 * counter ** 2
    if electrons < equation and electrons != 0:
        shells.append(electrons)
        break
    shells.append(equation)
    electrons -= equation

print(shells)
