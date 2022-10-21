number = int(input())

for i in range(97, 97 + number):
    for k in range(97, 97 + number):
        for g in range(97, 97 + number):
            print(f"{chr(i)}{chr(k)}{chr(g)}")