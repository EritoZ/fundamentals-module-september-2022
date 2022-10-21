number = int(input())
lines = int(input())
for i in range(lines):
    letter = input()
    print(chr(ord(letter) + number), end="")
