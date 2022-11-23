students_hour_employee1 = int(input())
students_hour_employee2 = int(input())
students_hour_employee3 = int(input())
students = int(input())
hours = 0

while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students -= students_hour_employee1 + students_hour_employee2 + students_hour_employee3

print(f"Time needed: {hours}h.")
