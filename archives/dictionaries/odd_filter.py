def convert_odd(even_num: int):

    if even_num > sum(array_integers) / len(array_integers):
        even_num += 1
    else:
        even_num -= 1

    return str(even_num)


array_integers = map(int, input().split())

array_integers = [num for num in array_integers if num % 2 == 0]

array_integers = " ".join(map(convert_odd, array_integers))

print(array_integers)
