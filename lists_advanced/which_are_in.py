sub_strings = input().split(", ")
strings = "".join(input().split(", "))

sub_strings = [string for string in sub_strings if string in strings]

print(sub_strings)
