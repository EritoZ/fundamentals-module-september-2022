number = int(input())

for i in range(1, number + 1):
    sum = 0
    for k in str(i):
        sum += int(k)
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
