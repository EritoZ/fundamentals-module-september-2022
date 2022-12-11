def card_value(card):
    power_type_dict = {"1": 10, "J": 11, "Q": 12, "K": 13, "A": 14, "S": 4, "H": 3, "D": 2, "C": 1}

    power = card[0]
    type = power_type_dict[card[-1]]

    if power in power_type_dict:
        power = power_type_dict[power]

    value = int(power) * type

    return value


player_cards = {}

command = input()
while command != "JOKER":
    name, cards = command.split(": ")
    cards = cards.split(", ")

    if name not in player_cards:
        player_cards[name] = []
    [player_cards[name].append(card) for card in cards if card not in player_cards[name]]

    command = input()

for name in player_cards:
    total = sum([card_value(card) for card in player_cards[name]])
    print(f"{name}: {total}")
