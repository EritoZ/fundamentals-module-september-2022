courses = {}

command = input()
while command != "end":
    course, student = command.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    command = input()

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
