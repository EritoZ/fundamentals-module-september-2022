numbers = input().split(", ")

positive_numbers = [n for n in numbers if int(n) >= 0]
negative_numbers = [n for n in numbers if int(n) < 0]
even_numbers = [n for n in numbers if int(n) % 2 == 0]
odd_numbers = [n for n in numbers if int(n) % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
