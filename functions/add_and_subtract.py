def sum_numbers(n1, n2,):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def add_and_subtract(n1, n2, n3):
    result = sum_numbers(n1, n2)
    return subtract(result, n3)


number_first = int(input())
number_second = int(input())
number_third = int(input())

print(add_and_subtract(number_first, number_second, number_third))
