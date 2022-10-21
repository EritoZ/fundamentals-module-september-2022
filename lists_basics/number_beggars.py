integers = input()
beggars = int(input())
integers = integers.split(", ")
counter = 0
beggar_cages = []

for _ in range(beggars):
    beggar_cages.append([])

for i in range(len(integers)):
    beggar_cages[counter].append(int(integers[i]))

    counter += 1

    if counter == beggars:
        counter = 0

for cage in range(len(beggar_cages)):
    if len(beggar_cages[cage]) == 0:
        beggar_cages[cage] = 0
    else:
        sum_numbers = 0
        while len(beggar_cages[cage]) > 0:
            sum_numbers += beggar_cages[cage][0]
            beggar_cages[cage].pop(0)

        beggar_cages[cage] = sum_numbers

print(beggar_cages)
