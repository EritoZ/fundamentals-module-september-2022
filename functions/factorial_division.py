def factorial_division(first_int: int, second_int: int):
    factorial_n1 = 1
    factorial_n2 = 1
    for number in range(2, first_int + 1):
        factorial_n1 *= number

    for number in range(2, second_int + 1):
        factorial_n2 *= number

    return factorial_n1 / factorial_n2


first_number = int(input())
second_number = int(input())

print(f"{factorial_division(first_number, second_number):.2f}")
