people = int(input())
elevator_capacity = int(input())
courses = 0

courses += people // elevator_capacity
if people % elevator_capacity > 0:
    courses += 1

print(courses)