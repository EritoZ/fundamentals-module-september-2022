def tribonacci_sequence(integer):
    lst = [1]
    three_indexes = [1]
    for i in range(integer - 1):
        lst.append(sum(three_indexes))
        three_indexes.append(sum(three_indexes))
        if len(three_indexes) == 4:
            three_indexes.pop(0)

    return " ".join(list(map(str, lst)))


number = int(input())

print(tribonacci_sequence(number))
