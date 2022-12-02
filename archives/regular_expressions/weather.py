import re

weather_dict = {}
valid_weather_pattern = r"([A-Z]{2})(\d+\.\d+)([A-Za-z]+)\|"

command = input()
while command != "end":
    weather = command

    valid_weather = re.search(valid_weather_pattern, weather)

    if valid_weather:
        city, temp, type_weather = valid_weather.group(1), float(valid_weather.group(2)), valid_weather.group(3)

        weather_dict[city] = [temp, type_weather]

    command = input()

weather_dict = dict(sorted(weather_dict.items(), key=lambda city: city[1][0]))

for city in weather_dict:
    print(f"{city} => {weather_dict[city][0]:.2f} => {weather_dict[city][1]}")
