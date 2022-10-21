words = input().split(" ")

for word in range(len(words)):
    element = ""
    new_word = []
    numbers = True
    for letter in words[word]:
        if 48 <= ord(letter) <= 57:
            element += letter
        else:
            if numbers:
                elements = chr(int(element))
                new_word.append(elements)
                numbers = False
            new_word.append(letter)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    words[word] = "".join(new_word)

print(*words, sep=" ")
