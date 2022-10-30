class Weapon:
    bullets = 0

    def __init__(self, bullets: int):
        Weapon.bullets = bullets

    def shoot(self):
        if Weapon.bullets:
            Weapon.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {Weapon.bullets}"


weapon = Weapon(int(input()))

while True:
    command = input()
    if command == "weapon":
        print(weapon)
    elif command == "shoot":
        print(weapon.shoot())
    elif command == "end":
        break
    else:
        print("Invalid command")
