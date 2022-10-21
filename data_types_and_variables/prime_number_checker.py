number = int(input())
is_prime_number = False

for i in range(2, number):
    if number % i == 0:
        break
else:
    is_prime_number = True

if is_prime_number:
    print(is_prime_number)
else:
    print(is_prime_number)
