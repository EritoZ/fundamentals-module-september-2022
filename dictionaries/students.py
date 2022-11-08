students = {}

command = input()
while ":" in command:
    command = command.split(":")
    name, id, course = command
    students[name] = [id, course]

    command = input()

filter_course = " ".join(command.split("_"))

[print(f"{student} - {students[student][0]}") for student in students.keys() if filter_course in students[student]]
