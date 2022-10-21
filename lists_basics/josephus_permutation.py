people_in_circle = input().split(" ")
execution_index = int(input())
new_circle = []
deaded = []
counter = 0

while len(people_in_circle) > 0:
    for i in range(len(people_in_circle)):
        counter += 1
        if counter % execution_index == 0:
            deaded.append(people_in_circle[i])
            counter = 0
        else:
            new_circle.append(people_in_circle[i])

    people_in_circle = new_circle
    new_circle = []
    if len(people_in_circle) == 1:
        deaded.append(people_in_circle.pop(0))

print(f"[{','.join(deaded)}]")
