import re

text = input()
coolness_threshold = 0

valid_emojis = re.findall(r"(::|\*\*)([A-Z][a-z]{2,})\1", text)

all_digits = re.findall(r"\d", text)

for i, digit in enumerate(all_digits):
    if i == 0:
        coolness_threshold += int(digit)
    else:
        coolness_threshold *= int(digit)

print(f"""Cool threshold: {coolness_threshold}
{len(valid_emojis)} emojis found in the text. The cool ones are:""")
for emoji in valid_emojis:
    coolness = sum(map(ord, emoji[1]))
    if coolness >= coolness_threshold:
        print("".join(emoji) + emoji[0])
