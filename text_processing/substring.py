delete = input()
text = input()

while delete in text:
    text = text.replace(delete, "")

print(text)
