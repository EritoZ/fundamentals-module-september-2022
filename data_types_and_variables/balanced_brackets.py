lines = int(input())
balanced = True
counter = 0
for i in range(lines):
    string = input()
    if string != "(" and string != ")":
        continue
    elif string == "(" and counter == 0:
        counter += 1
    elif string == ")" and counter == 1:
        counter = 0
    else:
        balanced = False
        break

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
