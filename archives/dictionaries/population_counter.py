countries_dict = {}

command = input()
while command != "report":
    city, country, population = command.split("|")

    if country not in countries_dict:
        countries_dict[country] = {}
    countries_dict[country][city] = int(population)

    command = input()

countries_dict = dict(sorted(countries_dict.items(), key=lambda countries: sum(countries[1].values()), reverse=True))

new_row = "\n"
for country in countries_dict:
    countries_dict[country] = dict(sorted(countries_dict[country].items(), key=lambda cities: cities[1], reverse=True))

    print(f"""{country} (total population: {sum(countries_dict[country].values())})
{new_row.join([f'=>{city}: {countries_dict[country][city]}' for city in countries_dict[country]])}""")
