characters = input().split(", ")
dictionary = {character: ord(character) for character in characters}
print(dictionary)
