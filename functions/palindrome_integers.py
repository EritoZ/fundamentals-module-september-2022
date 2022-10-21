def palindrome_checker(numbers: str):
    true_false = ""
    numbers = numbers.split(", ")
    for n in numbers:
        reverse_n = ""
        for i in range(len(n) - 1, -1, -1):
            reverse_n += n[i]
        if n == reverse_n:
            true_false += "True\n"
        else:
            true_false += "False\n"

    return true_false


integers = input()

print(palindrome_checker(integers))
