car_dict = {}
cars_number = int(input())

for automobile in range(cars_number):
    data = input().split("|")
    car, mileage, fuel = data[0], int(data[1]), int(data[2])

    car_dict[car] = [mileage, fuel]

command = input()
while command != "Stop":
    command = command.split(" : ")
    instruction = command[0]
    the_car = command[1]

    if instruction == "Drive":
        distance = int(command[2])
        fuel_needed = int(command[3])

        if car_dict[the_car][1] >= fuel_needed:
            car_dict[the_car][0] += distance
            car_dict[the_car][1] -= fuel_needed
            print(f"{the_car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if car_dict[the_car][0] >= 100000:
            car_dict.pop(the_car)
            print(f"Time to sell the {the_car}!")

    elif instruction == "Refuel":
        fuel_needed_refuel = int(command[2])

        if car_dict[the_car][1] + fuel_needed_refuel > 75:
            fuel_needed_refuel = 75 - car_dict[the_car][1]
            car_dict[the_car][1] = 75
        else:
            car_dict[the_car][1] += fuel_needed_refuel

        print(f"{the_car} refueled with {fuel_needed_refuel} liters")

    elif instruction == "Revert":
        kilometers = int(command[2])

        if car_dict[the_car][0] - kilometers >= 10000:
            car_dict[the_car][0] -= kilometers
            print(f"{the_car} mileage decreased by {kilometers} kilometers")
        else:
            car_dict[the_car][0] = 10000

    command= input()

for car in car_dict:
    print(f"{car} -> Mileage: {car_dict[car][0]} kms, Fuel in the tank: {car_dict[car][1]} lt.")
