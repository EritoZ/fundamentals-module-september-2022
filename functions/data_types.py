def data_types(string_type, element):
    if string_type == "int":
        return int(element) * 2
    elif string_type == "real":
        return f"{float(element) * 1.5:.2f}"
    elif string_type == "string":
        return f"${element}$"


type_string = input()
symbol = input()

print(data_types(type_string, symbol))
