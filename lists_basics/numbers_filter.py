lines = int(input())
lst = []
filtered_lst = []

for i in range(lines):
    n = int(input())
    lst.append(n)

command = input()

for number in lst:
    filtered_pass = (
        (command == "even" and number % 2 == 0) or
        (command == "odd" and number % 2 != 0) or
        (command == "negative" and number < 0) or
        (command == "positive" and number >= 0)
    )
    if filtered_pass:
        filtered_lst.append(number)

print(filtered_lst)
