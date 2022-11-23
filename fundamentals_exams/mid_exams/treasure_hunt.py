def loot(current_treasure_state, strings):
    strings = [item for item in strings if item not in current_treasure_state]
    for item in strings:
        current_treasure_state.insert(0, item)

    return current_treasure_state


def drop(current_treasure_state, item_index):
    current_treasure_state.append(current_treasure_state.pop(item_index))

    return current_treasure_state


def steal(current_treasure_state, count):
    if count >= len(current_treasure_state):
        stolen_items = current_treasure_state[:]
        current_treasure_state = []
    else:
        stolen_items = current_treasure_state[len(current_treasure_state) - count:]
        current_treasure_state = current_treasure_state[:len(current_treasure_state) - count]

    return current_treasure_state, stolen_items


treasure_state = input().split("|")

command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]

    if action == "Loot":
        command.pop(0)
        items = command
        treasure_state = loot(treasure_state, items)
    elif action == "Drop":
        index = int(command[1])
        if index in range(len(treasure_state)):
            treasure_state = drop(treasure_state, index)
    elif action == "Steal":
        count_items = int(command[1])
        treasure_state, stolen = steal(treasure_state, count_items)
        print(", ".join(stolen))

    command = input()

if not treasure_state:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = sum([len(item) for item in treasure_state]) / len(treasure_state)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
