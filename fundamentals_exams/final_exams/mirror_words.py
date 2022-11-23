import re

pairs = []
text = input()
mirrors = False
pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

valid_pairs = re.findall(pattern, text)

if valid_pairs:
    print(f"{len(valid_pairs)} word pairs found!")
    for pair in valid_pairs:
        if pair[1] == pair[2][::-1]:
            mirrors = True
            pairs.append(f"{pair[1]} <=> {pair[2]}")
else:
    print("No word pairs found!")

if mirrors:
    print(f"""The mirror words are:
{", ".join(pairs)}""")

else:
    print("No mirror words!")