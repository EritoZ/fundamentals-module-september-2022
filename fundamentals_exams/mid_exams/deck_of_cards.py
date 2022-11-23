def add(cards, card_name):
    cards.append(card_name)

    return cards


def remove(cards, card_name):
    cards.remove(card_name)

    return cards


def remove_at(cards, index):
    cards.pop(index)

    return cards


def insert(cards, card_name, index):
    cards.insert(index, card_name)

    return cards


initial_cards = input().split(", ")
number = int(input())

for i in range(number):
    command = input().split(", ")
    action = command[0]

    if action == "Add":
        card = command[1]
        if card in initial_cards:
            print("Card is already in the deck")
        else:
            initial_cards = add(initial_cards, card)
            print("Card successfully added")
    elif action == "Remove":
        card = command[1]
        if card in initial_cards:
            initial_cards = remove(initial_cards, card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        card_index = int(command[1])
        if card_index in range(len(initial_cards)):
            initial_cards = remove_at(initial_cards, card_index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    else:
        card_index = int(command[1])
        card = command[2]
        if card_index in range(len(initial_cards)) and card not in initial_cards:
            initial_cards = insert(initial_cards, card, card_index)
            print("Card successfully added")
        elif card_index not in range(len(initial_cards)):
            print("Index out of range")
        else:
            print("Card is already added")

print(", ".join(initial_cards))
