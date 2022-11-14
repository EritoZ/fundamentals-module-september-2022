characters = input()

mutated_characters = [chr(ord(character) + 3) for character in characters]

print("".join(mutated_characters))
