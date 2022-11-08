words = input().split()
words = [word.lower() for word in words]
words_dictionary = {word: words.count(word) for word in words}
[print(word) for word in words_dictionary if words_dictionary[word] % 2 != 0]
