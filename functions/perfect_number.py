def perfect_number_checker(num: int):
    lst = []
    for n in range(1, num):
        if num % n == 0:
            lst.append(n)

    if sum(lst) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


integer = int(input())

print(perfect_number_checker(integer))
