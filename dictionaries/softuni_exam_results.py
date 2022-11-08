student_results = {}
student_submission = {}

command = input()
while command != "exam finished":
    command = command.split("-")

    if "banned" in command:
        username = command[0]
        student_results.pop(username)
    else:
        username, language, points = command[0], command[1], int(command[2])
        if username in student_results and student_results[username][0] == language:
            if student_results[username][1] < points:
                student_results[username] = [language, points]
        else:
            student_results[username] = [language, points]
            if language not in student_submission:
                student_submission[language] = 0
        student_submission[language] += 1

    command = input()

print("Results:")
[print(f"{username} | {data[1]}") for username, data in student_results.items()]
print("Submissions:")
[print(f"{language} - {points}") for language, points in student_submission.items()]
