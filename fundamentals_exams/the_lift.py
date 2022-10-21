people = int(input())
lift_state = input().split(" ")
no_people = False

for i in range(len(lift_state)):
    space = int(lift_state[i])
    while space < 4:
        space += 1
        people -= 1
        if people == 0:
            no_people = True
            break
    lift_state[i] = str(space)
    if no_people:
        break


if no_people and sum(list(map(int, lift_state))) == len(lift_state) * 4:
    print(f"{' '.join(lift_state)}")
elif no_people:
    print(f"""The lift has empty spots!
{" ".join(lift_state)}
""")
else:
    print(f"""There isn't enough space! {people} people in a queue!
{" ".join(lift_state)}
""")
