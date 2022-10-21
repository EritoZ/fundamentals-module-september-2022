people = int(input())
lift_state = list(map(int, input().split(" ")))
no_people = False

for space in range(len(lift_state)):
    while lift_state[space] < 4:
        lift_state[space] += 1
        people -= 1
        if people == 0:
            no_people = True
            break
    if no_people:
        break

if no_people and sum(lift_state) == len(lift_state) * 4:
    print(f"{' '.join(map(str, lift_state))}")
elif no_people:
    print(f"""The lift has empty spots!
{" ".join(map(str, lift_state))}
""")
else:
    print(f"""There isn't enough space! {people} people in a queue!
{" ".join(map(str, lift_state))}
""")
