string = input()
string = string.split(" ")

for i, number in enumerate(string):
    string[i] = int(number) * -1

print(string)
