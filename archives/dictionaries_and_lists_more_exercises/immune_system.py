immune_system_health = int(input())
initial_health = immune_system_health
defeated = False
virus_dict = {}

command = input()
while command != "end":
    virus = command
    virus_strength = int(sum(map(ord, virus)) / 3)
    virus_defeat_time = virus_strength * len(virus)

    if virus not in virus_dict:
        virus_dict[virus] = {"counter": 1}

    elif virus_dict[virus]["counter"] < 2:
        virus_dict[virus]["counter"] += 1
        virus_defeat_time = int(virus_defeat_time / 3)

    print(f"Virus {virus}: {virus_strength} => {virus_defeat_time} seconds")

    if immune_system_health >= virus_defeat_time:
        immune_system_health -= virus_defeat_time

        print(f"{virus} defeated in {virus_defeat_time // 60}m {virus_defeat_time % 60}s.")
        print(f"Remaining health: {immune_system_health}")
    else:
        print(f"Immune System Defeated.")
        defeated = True
        break

    if immune_system_health + immune_system_health * 0.2 > initial_health:
        immune_system_health = initial_health
    else:
        immune_system_health += int(immune_system_health * 0.2)

    command = input()

if not defeated:
    print(f"Final Health: {immune_system_health}")
