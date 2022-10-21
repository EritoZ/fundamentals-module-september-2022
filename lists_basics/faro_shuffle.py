cards = input()
shuffles = int(input())
lst1 = []
lst2 = []
shuffled_cards = []

cards = cards.split(" ")

for shuffle in range(shuffles):
    for i in range(len(cards)):
        if i < len(cards) // 2:
            lst1.append(cards[i])
        else:
            lst2.append(cards[i])

    for i in range(len(cards) // 2):
        shuffled_cards.append(lst1[i])
        shuffled_cards.append(lst2[i])

    cards = shuffled_cards
    lst1.clear()
    lst2.clear()
    shuffled_cards = []

print(cards)
