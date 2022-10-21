import math


def longer_line(list1, list2, list3, list4):
    line1 = []
    line2 = []
    point1_sum = 0
    point2_sum = 0
    point3_sum = 0
    point4_sum = 0
    for point in list1:
        line1.append(abs(float(point)))
        point1_sum += abs(float(point))
    for point in list2:
        line1.append(abs(float(point)))
        point2_sum += abs(float(point))
    for point in list3:
        line2.append(abs(float(point)))
        point3_sum += abs(float(point))
    for point in list4:
        line2.append(abs(float(point)))
        point4_sum += abs(float(point))

    line1_sum = sum(line1)
    line2_sum = sum(line2)

    new_lists = []
    original_list = list1 + list2 + list3 + list4
    counter = 0
    new_list = []
    for i in original_list:
        counter += 1
        new_list.append(str(math.floor(float(i))))
        if counter % 2 == 0:
            new_lists.append(new_list)
            new_list = []

    if line1_sum >= line2_sum:
        if point1_sum <= point2_sum:
            return f"({', '.join(new_lists[0])})({', '.join(new_lists[1])})"
        else:
            return f"({', '.join(new_lists[1])})({', '.join(new_lists[0])})"
    else:
        if point3_sum <= point4_sum:
            return f"({', '.join(new_lists[2])})({', '.join(new_lists[3])})"
        else:
            return f"({', '.join(new_lists[3])})({', '.join(new_lists[2])})"


number1 = input()
number2 = input()
number3 = input()
number4 = input()
number5 = input()
number6 = input()
number7 = input()
number8 = input()

print(longer_line([number1, number2], [number3, number4], [number5, number6], [number7, number8]))
