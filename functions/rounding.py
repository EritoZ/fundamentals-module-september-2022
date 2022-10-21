def round_multiple(numbers: str):
    numbers = list(map(float, numbers.split(" ")))

    for i, number in enumerate(numbers):
        numbers[i] = round(number)

    return numbers


ns = input()

print(round_multiple(ns))
