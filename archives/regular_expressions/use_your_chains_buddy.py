import re


def mutate_letter(character):
    if ord(character) in range(97, 110):
        return chr(ord(character) + 13)
    elif ord(character) in range(110, 123):
        return chr(ord(character) - 13)
    else:
        return character


html = input()
p_tag_info = "".join(re.findall(r"<p>(.+?)</p>", html))

p_tag_info = re.sub(r"[^a-z0-9]+", " ", p_tag_info)

p_tag_info = "".join(map(mutate_letter, p_tag_info))

print(p_tag_info)
