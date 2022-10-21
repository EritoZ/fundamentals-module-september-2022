numbers = input().split(", ")
lst = []
counter = 0

for number in numbers:
    if number == "0":
        counter += 1
    else:
        lst.append(int(number))

lst += [0] * counter

print(lst)
