def loading_bar(integer: int):
    times = number // 10
    rest = 10 - times
    load = "%" * times + "." * rest

    return f"[{load}]"


number = int(input())

if number < 100:
    print(f"""{number}% {loading_bar(number)}
Still loading...
""")
else:
    print(f"""100% Complete!
{loading_bar(number)}
""")
