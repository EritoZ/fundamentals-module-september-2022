countries = input().split(", ")
capitals = input().split(", ")

countries_with_capitals = {countries[i]: capitals[i] for i in range(len(countries))}

[print(f"{country} -> {countries_with_capitals[country]}") for country in countries_with_capitals]
