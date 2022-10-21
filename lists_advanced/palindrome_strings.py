words = [word for word in input().split(" ") if "".join(reversed(word)) == word]
palindrome = input()

print(words)
print(f"Found palindrome {words.count(palindrome)} times")