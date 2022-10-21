n1 = int(input())
n2 = int(input())
n3 = int(input())
zero = False

lst_int = [n1, n2, n3]

counter = 0
for i in range(len(lst_int)):
    if lst_int[i] < 0:
        counter += 1
    elif lst_int[i] == 0:
        zero = True
        break

if zero:
    print("zero")
elif counter == 0:
    print("positive")
elif counter % 2 != 0:
    print("negative")
else:
    print("positive")
