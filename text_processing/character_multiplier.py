word1, word2 = input().split()
total = 0

for character in word1[:len(word2)]:
    total += ord(character) * ord(word2[0])
    word1 = word1.replace(word1[0], "", 1)
    word2 = word2.replace(word2[0], "", 1)

total += sum(ord(character) for character in word1 + word2)

print(total)
