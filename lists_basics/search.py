lines = int(input())
word = input()
unfiltered_lst = []
filtered_lst = []

for i in range(lines):
    string = input()
    unfiltered_lst.append(string)
    if word in string:
        filtered_lst.append(string)

print(f"""{unfiltered_lst}
{filtered_lst}""")
