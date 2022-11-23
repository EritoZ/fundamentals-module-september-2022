piece_dictionary = {}
pieces_amount = int(input())

for _ in range(pieces_amount):
    data = input().split("|")
    piece, composer, key = data[0], data[1], data[2]

    piece_dictionary[piece] = [composer, key]

command = input()
while command != "Stop":
    data = command.split("|")
    command = data[0]
    piece = data[1]

    if command == "Add":
        composer = data[2]
        key = data[3]

        if piece not in piece_dictionary:
            piece_dictionary[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command == "Remove":

        if piece in piece_dictionary:
            piece_dictionary.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = data[2]

        if piece in piece_dictionary:
            piece_dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece in piece_dictionary:
    print(f"{piece} -> Composer: {piece_dictionary[piece][0]}, Key: {piece_dictionary[piece][1]}")
