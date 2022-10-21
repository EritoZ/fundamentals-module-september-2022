factor = int(input())
count = int(input())
lst = []
n = 0

for number in range(count):
    n += factor
    lst.append(n)

print(lst)
