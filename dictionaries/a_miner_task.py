dictionary = {}

command = input()
while command != "stop":
    resource = command

    if resource not in dictionary:
        dictionary[resource] = 0
    dictionary[resource] += int(input())

    command = input()

[print(f"{resource} -> {dictionary[resource]}") for resource in dictionary]
