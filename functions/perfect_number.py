def perfect_number_checker(num: int):
    lst = []
    for n in range(1, num):
        if num % n == 0:
            lst.append(n)

    return sum(lst)


integer = int(input())

print(perfect_number_checker(integer))
