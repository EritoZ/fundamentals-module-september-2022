employees = list(map(int, input().split(" ")))
happiness_factor = int(input())

employees = [happiness * happiness_factor for happiness in employees]

average_happiness = sum(employees) / len(employees)

happier_employees = len(list(filter(lambda x: x >= average_happiness, employees)))

if happier_employees >= len(employees) // 2:
    print(f"Score: {happier_employees}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {happier_employees}/{len(employees)}. Employees are not happy!")
