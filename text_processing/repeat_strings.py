strings = input().split()

strings = [string * len(string) for string in strings]

print("".join(strings))
