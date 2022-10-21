priorities = []

command = input()
while command != "End":
    command = command.split("-")

    index = int(command[0])
    event = command[1]

    priorities.append([index, event])

    command = input()

priorities = [event[1] for event in sorted(priorities)]

print(priorities)
