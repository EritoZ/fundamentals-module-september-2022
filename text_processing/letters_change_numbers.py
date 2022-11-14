letters_with_numbers = input().split()
total_sum = 0

for letters_and_numbers in letters_with_numbers:
    current_number = ""
    left_row = []
    right_row = []
    got_the_number = False

    for something in letters_and_numbers:

        if something.isdigit():
            got_the_number = True
            current_number += something
        elif something.isalpha() and not got_the_number:
            left_row.append(something)
        else:
            right_row.append(something)

    current_number = int(current_number)
    for i, letter in enumerate(left_row):

        if letter.isupper():
            current_number /= ord(letter) - 64
        else:
            current_number *= ord(letter) - 96

        if right_row[i].isupper():
            current_number -= ord(right_row[i]) - 64
        else:
            current_number += ord(right_row[i]) - 96

    total_sum += current_number

print(f"{total_sum:.2f}")
