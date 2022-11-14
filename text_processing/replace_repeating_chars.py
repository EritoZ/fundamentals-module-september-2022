strings = input()

print("".join([character for i, character in enumerate(strings) if i == 0 or strings[i - 1] != character]))
