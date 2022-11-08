student_grades = {}

number_of_students = int(input())

for _ in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for student in student_grades:
    student_grades[student] = sum(student_grades[student]) / len(student_grades[student])

[print(f"{student} -> {student_grades[student]:.2f}") for student in student_grades if student_grades[student] >= 4.50]
