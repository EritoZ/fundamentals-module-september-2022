import re

srabsko_dict = {}

command = input()
while command != "End":
    valid_data = re.search(r"(?P<singer>.+?(?: .+?){0,2}) @(?P<venue>.+?(?: .+?){0,2})"
                           r"\s(?P<ticket_price>\d+) (?P<tickets_count>\d+)", command)

    if valid_data:
        singer = valid_data.group("singer")
        venue = valid_data.group("venue")
        ticket_price = int(valid_data.group("ticket_price"))
        tickets_count = int(valid_data.group("tickets_count"))

        if venue not in srabsko_dict:
            srabsko_dict[venue] = {}

        if singer not in srabsko_dict[venue]:
            srabsko_dict[venue][singer] = 0

        srabsko_dict[venue][singer] += ticket_price * tickets_count

    command = input()

for venue in srabsko_dict:
    srabsko_dict[venue] = dict(sorted(srabsko_dict[venue].items(), key=lambda pevets: pevets[1], reverse=True))

    print(venue)
    print("\n".join([f"#  {singer} -> {srabsko_dict[venue][singer]}" for singer in srabsko_dict[venue]]))
