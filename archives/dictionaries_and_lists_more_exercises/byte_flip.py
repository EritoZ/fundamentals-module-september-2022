def hex_to_dec(hex_num):
    letter_to_num = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    total = 0
    for i, character in enumerate(hex_num[::-1]):
        if character in letter_to_num:
            character = letter_to_num[character]

        total += int(character) * 16 ** i

    return total


string_array = input().split()

string_array = [el for el in string_array if len(el) == 2]

string_array = [el[::-1] for el in string_array]

string_array.reverse()

string_array = list(map(hex_to_dec, string_array))

print("".join(map(chr, string_array)))
