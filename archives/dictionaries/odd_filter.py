def convert_odd(even_num: int, array):

    if even_num > sum(array) / len(array):
        even_num += 1
    else:
        even_num -= 1

    return str(even_num)


def odd_filter(array):
    
    array = [num for num in array if num % 2 == 0]

    array = [convert_odd(num, array) for num in array]
    
    return array


array_integers = map(int, input().split())

array_integers = odd_filter(array_integers)

print(" ".join(array_integers))
