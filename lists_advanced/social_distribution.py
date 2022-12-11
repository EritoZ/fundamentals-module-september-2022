population = list(map(int, input().split(", ")))
min_wealth = int(input())
no_equal = False

for family in range(len(population)):
    richest = population.index(max(population))

    while population[family] < min_wealth:
        if max(population) <= min_wealth:
            no_equal = True
            break

        population[family] += 1
        population[richest] -= 1

    if no_equal:
        break

if not no_equal:
    print(population)
else:
    print("No equal distribution possible")
