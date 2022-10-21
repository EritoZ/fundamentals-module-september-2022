numbers = list(map(int, input().split(", ")))
tens = 0

while numbers:
    tens += 10
    current_list = list(filter(lambda n: n <= tens, numbers))
    numbers = [num for num in numbers if num not in current_list]
    print(f"Group of {tens}'s: {current_list}")