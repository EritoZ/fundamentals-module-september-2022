def ascii_between_nums(chr1, ch2):
    lst = []
    for n in range(ord(chr1) + 1, ord(ch2)):
        lst += chr(n)

    return " ".join(lst)


symbol1 = input()
symbol2 = input()

print(ascii_between_nums(symbol1, symbol2))
