def collect(items, item):
    items.append(item)

    return items


def drop(items, item):
    items.remove(item)

    return items


def combine(items, item1, item2):
    position_item1 = items.index(item1)
    items.insert(position_item1 + 1, item2)

    return items


def renew(items, item):
    items.remove(item)
    items.append(item)

    return items


journal = input().split(", ")

command = input()
while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item_or_items = command[1]

    if action == "Collect":
        if item_or_items not in journal:
            journal = collect(journal, item_or_items)
    elif action == "Drop":
        if item_or_items in journal:
            journal = drop(journal, item_or_items)
    elif action == "Combine Items":
        item_or_items = item_or_items.split(":")
        old_item = item_or_items[0]
        new_item = item_or_items[1]
        if old_item in journal:
            journal = combine(journal, old_item, new_item)
    elif action == "Renew":
        if item_or_items in journal:
            journal = renew(journal, item_or_items)

    command = input()

print(", ".join(journal))
