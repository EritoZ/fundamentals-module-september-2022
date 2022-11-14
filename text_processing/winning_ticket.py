def check_side(side):
    repeated_elements = []
    current_repeated_element = ""
    element_to_repeat = ""
    for el in side:
        if element_to_repeat != el:
            if el in ["@", "#", "$", "^"]:
                if current_repeated_element:
                    repeated_elements.append(current_repeated_element)
                    current_repeated_element = ""
                element_to_repeat = el
                current_repeated_element += el
            else:
                if current_repeated_element:
                    repeated_elements.append(current_repeated_element)
                    current_repeated_element = ""
        else:
            current_repeated_element += el

    repeated_elements.append(current_repeated_element)

    return repeated_elements


lottery_tickets = input().split(", ")

for ticket in lottery_tickets:
    ticket = ticket.strip()

    if len(ticket) == 20:
        first_side = ticket[:10]
        second_side = ticket[10:]
        if len(set(ticket)) == 1 and ticket[0] in ["@", "#", "$", "^"]:
            print(f"ticket \"{ticket}\" - {len(first_side)}{ticket[0]} Jackpot!")
        else:
            repeated_elements_side1 = check_side(first_side)
            repeated_elements_side2 = check_side(second_side)
            both_sides = sorted(repeated_elements_side1 + repeated_elements_side2, key=lambda x: len(x), reverse=True)

            if (
                    len(both_sides[0]) >= 6
                    and len(both_sides[1]) >= 6
                    and both_sides[0][0] == both_sides[1][0]
            ):
                print(f"ticket \"{ticket}\" - {len(both_sides[1])}{both_sides[0][0]}")
            else:
                print(f"ticket \"{ticket}\" - no match")
    else:
        print("invalid ticket")
