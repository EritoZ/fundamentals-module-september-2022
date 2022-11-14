number_of_lines = int(input())

for line in range(number_of_lines):
    sentence = input()
    name = []
    age = []
    its_name = False
    its_age = False
    for symbol in sentence:
        if symbol == "@":
            its_name = True
            continue
        elif symbol == "|":
            its_name = False
        elif symbol == "#":
            its_age = True
            continue
        elif symbol == "*":
            its_age = False

        if its_name:
            name.append(symbol)
        elif its_age:
            age.append(symbol)

    print(f"{''.join(name)} is {''.join(age)} years old.")
