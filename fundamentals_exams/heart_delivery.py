even_integers = list(map(int, input().split("@")))
position = 0
counter = 0

command = input()
while command != "Love!":
    command = command.split(" ")
    jump_length = int(command[1])

    position += jump_length

    if position >= len(even_integers):
        position = 0

    if even_integers[position] == 0:
        print(f"Place {position} already had Valentine's day.")
        command = input()
        continue

    even_integers[position] = even_integers[position] - 2

    if even_integers[position] == 0:
        print(f"Place {position} has Valentine's day.")
        counter += 1

    command = input()


print(f"Cupid's last position was {position}.")
if counter == len(even_integers):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(even_integers) - counter} places.")
