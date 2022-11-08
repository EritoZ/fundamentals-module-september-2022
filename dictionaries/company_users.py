companies = {}

command = input()
while command != "End":
    company, employee_id = command.split(" -> ")

    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

    command = input()

for company in companies:
    print(company)
    for employee_id in companies[company]:
        print(f"-- {employee_id}")
