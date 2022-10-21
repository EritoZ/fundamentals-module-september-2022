numbers = list(map(float, input().split(" ")))

for i, number in enumerate(numbers):
    numbers[i] = abs(number)

print(numbers)