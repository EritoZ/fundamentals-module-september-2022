first_char = input()
second_char = input()
the_string = input()

total_sum = sum([ord(char) for char in the_string if ord(char) in range(ord(first_char) + 1, ord(second_char))])

print(total_sum)
