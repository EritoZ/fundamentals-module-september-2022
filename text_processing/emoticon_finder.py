text = input()

[print(character + text[i + 1]) for i, character in enumerate(text) if character == ":"]
