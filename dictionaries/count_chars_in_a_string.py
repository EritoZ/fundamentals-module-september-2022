characters = input()
letter_dictionary = {}

for letter in characters:
    if letter not in letter_dictionary and letter != " ":
        letter_dictionary[letter] = characters.count(letter)

[print(f"{letter} -> {letter_dictionary[letter]}") for letter in letter_dictionary]
