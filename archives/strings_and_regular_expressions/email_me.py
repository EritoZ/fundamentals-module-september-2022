import re

email = input()

to_be_or_not_to_be = sum(map(ord, [*re.search(r".+(?=@)", email).group()]))\
                     - sum(map(ord, [*re.search(r"(?<=@).+", email).group()]))

if to_be_or_not_to_be >= 0:
    print("Call her!")
else:
    print("She is not the one.")
