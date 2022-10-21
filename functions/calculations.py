def calc(operator, n1, n2):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return int(n1 / n2)
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


operator = input()
number1 = int(input())
number2 = int(input())

print(calc(operator, number1, number2))
