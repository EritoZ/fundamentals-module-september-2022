dictionary = {}
words = int(input())

for word in range(words):
    word_key = input()
    synonym = input()

    if word_key not in dictionary:
        dictionary[word_key] = []
    dictionary[word_key].append(synonym)

[print(f"{word} - {', '.join(dictionary[word])}") for word in dictionary]
