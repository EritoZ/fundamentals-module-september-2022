hero_info = {}
heroes_amount = int(input())

for _ in range(heroes_amount):
    hero = input().split()
    hero_name = hero[0]

    hero_info[hero_name] = {"hp": int(hero[1]), "mp": int(hero[2])}

command = input()
while command != "End":
    command = command.split(" - ")
    action, name = command[0], command[1]

    if action == "CastSpell":
        mp_needed, spell_name = int(command[2]), command[3]

        if hero_info[name]["mp"] >= mp_needed:
            hero_info[name]["mp"] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {hero_info[name]['mp']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage, attacker = int(command[2]), command[3]

        hero_info[name]["hp"] -= damage
        if hero_info[name]["hp"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {hero_info[name]['hp']} HP left!")
        else:
            del hero_info[name]
            print(f"{name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount_mp = int(command[2])

        if hero_info[name]["mp"] + amount_mp > 200:
            amount_mp = 200 - hero_info[name]["mp"]
            hero_info[name]["mp"] = 200
        else:
            hero_info[name]["mp"] += amount_mp

        print(f"{name} recharged for {amount_mp} MP!")

    elif action == "Heal":
        amount_hp = int(command[2])

        if hero_info[name]["hp"] + amount_hp > 100:
            amount_hp = 100 - hero_info[name]["hp"]
            hero_info[name]["hp"] = 100
        else:
            hero_info[name]["hp"] += amount_hp

        print(f"{name} healed for {amount_hp} HP!")

    command = input()

for hero in hero_info:
    print(f"""{hero}
  HP: {hero_info[hero]["hp"]}
  MP: {hero_info[hero]["mp"]}""")
