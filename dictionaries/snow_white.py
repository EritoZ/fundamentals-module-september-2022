dwarf_dictionary = {}

command = input()
while command != "Once upon a time":
    command = command.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = command[0], command[1], int(command[2])

    dwarf_names = [dwarf[1] for dwarf in dwarf_dictionary]
    if dwarf_name not in dwarf_names:
        dwarf_dictionary[dwarf_hat_color, dwarf_name] = dwarf_physics
    else:
        dwarf_name_colours = [dwarf[0] for dwarf in dwarf_dictionary if dwarf[1] == dwarf_name]
        if dwarf_hat_color not in dwarf_name_colours:
            dwarf_dictionary[dwarf_hat_color, dwarf_name] = dwarf_physics
        else:
            if dwarf_physics > dwarf_dictionary[dwarf_hat_color, dwarf_name]:
                dwarf_dictionary[dwarf_hat_color, dwarf_name] = dwarf_physics

    command = input()

dwarf_colours = [dwarf[0] for dwarf in dwarf_dictionary]
dwarf_dictionary = dict(sorted(dwarf_dictionary.items(),
                               key=lambda dwarf: dwarf_colours.count(dwarf[0][0]), reverse=True))

dwarf_dictionary = dict(sorted(dwarf_dictionary.items(), key=lambda dwarf: dwarf[1], reverse=True))

for colour, dwarf in dwarf_dictionary:
    print(f"({colour}) {dwarf} <-> {dwarf_dictionary[colour, dwarf]}")
