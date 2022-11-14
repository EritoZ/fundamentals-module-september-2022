censored_words = input().split(", ")
text = input()

for word in censored_words:
    text = text.replace(word, "*" * len(word))

print(text)
