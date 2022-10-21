population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
no_distribution = False

person = 0
while min(population) < minimum_wealth:
    if population[person] < minimum_wealth:
        wealthiest = population.index(max(population))
        while population[person] < minimum_wealth:
            if max(population) > minimum_wealth:
                population[person] += 1
                population[wealthiest] -= 1
            else:
                no_distribution = True
                break
    person += 1

    if no_distribution:
        break

if no_distribution:
    print("No equal distribution possible")
else:
    print(population)
