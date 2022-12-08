a_string = input()
pattern = input()

while a_string.count(pattern) >= 2 and pattern:

    index_first_occurrence = a_string.index(pattern)
    a_string = a_string[:index_first_occurrence] + a_string[index_first_occurrence + len(pattern):]

    index_second_occurrence = a_string.rfind(pattern)
    a_string = a_string[:index_second_occurrence] + a_string[index_second_occurrence + len(pattern):]

    index_remove = len(pattern) // 2
    pattern = pattern[:index_remove] + pattern[index_remove + 1:]

    print("Shaked it.")

print("No shake.")
print(a_string)
