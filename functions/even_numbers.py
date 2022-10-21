def even_num(num):
    if num % 2 == 0:
        return True


numbers = list(map(int, input().split(" ")))

print(list(filter(even_num, numbers)))
