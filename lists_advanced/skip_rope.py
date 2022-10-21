a_string = input()
result = ""
its_over = False

numbers = list(filter(lambda n: 48 <= ord(n) <= 57, a_string))
elements = list(filter(lambda el: ord(el) < 48 or ord(el) > 57, a_string))

take_numbers = list(map(int, [numbers[n] for n in range(len(numbers)) if n % 2 == 0]))
skip_numbers = list(map(int, [numbers[n] for n in range(len(numbers) + 1) if n % 2 != 0]))

broken = False
while True:
    for i in range(take_numbers[0]):
        result += elements.pop(0)
        if not elements:
            broken = True
            break

    take_numbers.pop(0)

    if broken or not skip_numbers:
        break

    for i in range(skip_numbers[0]):
        elements.pop(0)
        if not elements:
            broken = True
            break

    skip_numbers.pop(0)

    if broken or not take_numbers:
        break

print(result)