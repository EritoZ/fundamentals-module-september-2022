import re


def mutate_letter(character):
    if ord(character) in range(97, 110):
        return chr(ord(character) + 13)
    elif ord(character) in range(110, 123):
        return chr(ord(character) - 13)
    else:
        return character


html = input()
p_tag_info = re.findall(r"<p>(.+?)</p>", html)

for i, p_tag in enumerate(p_tag_info):
    p_tag = re.sub(r"[^a-z0-9]+", " ", p_tag)
    p_tag_info[i] = "".join(map(mutate_letter, p_tag))

print("".join(p_tag_info))
