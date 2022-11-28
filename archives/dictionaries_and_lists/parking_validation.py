import re


def valid_plate(plate_info):
    if re.match(r"\b[A-Z]{2}\d{4}[A-Z]{2}\b", plate_info) is not None:
        return True
    else:
        print(f"ERROR: invalid license plate {plate_info}")
        return False


def one_car(cars, user):
    if user in cars:
        print(f"ERROR: already registered with plate number {cars[user]}")
        return False
    else:
        return True


def plate_not_in_cars(cars, plate_info):
    if plate_info in cars.values():
        print(f"ERROR: license plate {cars} is busy")
        return False
    else:
        return True


def plate_passes(cars, user, plate_info):
    if (
            one_car(cars, user)
            and valid_plate(plate_info)
            and plate_not_in_cars(cars, plate_info)
    ):
        print(f"{user} registered {plate_info} successfully")
        cars[user] = plate_info

    return cars


def in_database(cars, user):
    if user in cars:
        cars.pop(user)
        print(f"user {user} unregistered successfully")
    else:
        print(f"ERROR: user {user} not found")

    return cars


car_plates = {}
n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    current_command, username = command[0], command[1]

    if current_command == "register":
        license_plate = command[2]

        car_plates = plate_passes(car_plates, username, license_plate)

    elif current_command == "unregister":

        car_plates = in_database(car_plates, username)

for user in car_plates:
    print(f"{user} => {car_plates[user]}")
