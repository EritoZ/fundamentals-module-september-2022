import re

places = input()
valid_location = r"([=/])([A-Z][A-Za-z]{2,})\1"
travel_points = 0

valid_locations = re.findall(valid_location, places)

for place in valid_locations:
    travel_points += len(place[1])

print(f"Destinations: {', '.join([place[1] for place in valid_locations])}")
print(f"Travel Points: {travel_points}")
