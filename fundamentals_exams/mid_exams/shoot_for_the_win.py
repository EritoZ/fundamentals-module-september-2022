to_shoot = list(map(int, input().split(" ")))
shot_count = 0

command = input()
while command != "End":
    index_shot = int(command)

    if index_shot in range(len(to_shoot)):
        if to_shoot[index_shot] == -1:
            continue
        else:
            current_value = to_shoot[index_shot]
        for i, target in enumerate(to_shoot):
            if i == index_shot:
                to_shoot[i] = -1
            elif to_shoot[i] == -1:
                continue
            elif int(target) > current_value:
                to_shoot[i] = target - current_value
            else:
                to_shoot[i] = target + current_value

        shot_count += 1

    command = input()

print(f"Shot targets: {shot_count} -> {' '.join(list(map(str, to_shoot)))}")
