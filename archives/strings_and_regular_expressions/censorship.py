word = input()
sentence = input()

censored_sentence = sentence.replace(word, "*" * len(word))

print(censored_sentence)
