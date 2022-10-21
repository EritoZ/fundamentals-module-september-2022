year = int(input())
new_year = year
happy_year = False

while not happy_year:
    new_year += 1
    for i in range(len(str(new_year))):
        happy_year = True
        for k in range(len(str(new_year))):
            if str(new_year)[i] == str(new_year)[k] and i != k:
                happy_year = False
                break
        if not happy_year:
            break
print(new_year)