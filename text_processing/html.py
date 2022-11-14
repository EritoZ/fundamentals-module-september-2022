title = input()
content = input()

print(f"""<h1>
    {title}
</h1>""")
print(f"""<article>
    {content}
</article>""")

command = input()
while command != "end of comments":
    comment = command
    print(f"""<div>
    {comment}
</div>""")

    command = input()
