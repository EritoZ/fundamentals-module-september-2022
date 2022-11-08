contacts = {}

command = input()
while "-" in command:
    person, their_phone = command.split("-")
    contacts[person] = their_phone

    command = input()

number = int(command)

for i in range(number):
    contact = input()
    if contact in contacts:
        print(f"{contact} -> {contacts[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
