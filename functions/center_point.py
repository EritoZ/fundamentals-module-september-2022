import math


def closest_center_point(first_point, second_point, third_point, fourth_point):
    if sum([abs(first_point), abs(second_point)]) <= sum([abs(third_point), abs(fourth_point)]):
        return (math.floor(first_point), math.floor(second_point))
    else:
        return (math.floor(third_point), math.floor(fourth_point))


first_number = float(input())
second_number = float(input())
third_number = float(input())
fourth_number = float(input())

print(closest_center_point(first_number, second_number, third_number, fourth_number))
