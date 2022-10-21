def add(lesson, schedule):
    if lesson not in schedule:
        schedule.append(lesson)

    return schedule


def insert(lesson, index, schedule):
    if lesson not in schedule:
        schedule.insert(index, lesson)

    return schedule


def remove(lesson, schedule):
    if lesson in schedule:
        schedule.remove(lesson)
        if f"{lesson}-Exercise" in schedule:
            schedule.remove(f"{lesson}-Exercise")

    return schedule


def swap(lesson1, lesson2, schedule):
    if lesson1 in schedule and lesson2 in schedule:
        lesson1_index = schedule.index(lesson1)
        lesson2_index = schedule.index(lesson2)

        schedule[lesson1_index], schedule[lesson2_index] = schedule[lesson2_index], schedule[lesson1_index]
        if f"{lesson1}-Exercise" in schedule and f"{lesson2}-Exercise" in schedule:
            exercise1_index = schedule.index(f"{lesson1}-Exercise")
            exercise2_index = schedule.index(f"{lesson2}-Exercise")
            schedule[exercise1_index], schedule[exercise2_index] = schedule[exercise2_index], schedule[exercise1_index]

        elif f"{lesson1}-Exercise" in schedule:
            schedule.remove(f"{lesson1}-Exercise")
            schedule.insert(lesson2_index + 1, f"{lesson1}-Exercise")

        elif f"{lesson2}-Exercise" in schedule:
            schedule.remove(f"{lesson2}-Exercise")
            schedule.insert(lesson1_index + 1, f"{lesson2}-Exercise")

    return schedule


def exercise(lesson, schedule):
    if lesson in schedule and f"{lesson}-Exercise" not in schedule:
        lesson_index = schedule.index(lesson)
        schedule.insert(lesson_index + 1, f"{lesson}-Exercise")
    elif lesson not in schedule:
        schedule.append(lesson)
        schedule.append(f"{lesson}-Exercise")

    return schedule


initial_schedule = input().split(", ")

command = input()
while command != "course start":
    command = command.split(":")
    function = command[0]
    softuni_class = command[1]

    if function == "Add":
        initial_schedule = add(softuni_class, initial_schedule)

    elif function == "Insert":
        index_number = int(command[2])
        initial_schedule = insert(softuni_class, index_number, initial_schedule)

    elif function == "Remove":
        initial_schedule = remove(softuni_class, initial_schedule)

    elif function == "Swap":
        softuni_class2 = command[2]
        initial_schedule = swap(softuni_class, softuni_class2, initial_schedule)

    else:
        initial_schedule = exercise(softuni_class, initial_schedule)

    command = input()

for i, lesson in enumerate(initial_schedule):
    initial_schedule[i] = f"{i + 1}.{lesson}"

print('\n'.join(initial_schedule))
