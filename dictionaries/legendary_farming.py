def crafted(materials, material):
    materials[material] -= 250
    formatting = [f"{material}: {materials[material]}" for material in materials]

    return "\n".join(formatting)


legendary_item_materials = {"shards": 0, "fragments": 0, "motes": 0}
done = False

while not done:
    materials = input().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()

        if material == "shards":
            legendary_item_materials["shards"] += quantity
            if legendary_item_materials["shards"] >= 250:
                print("Shadowmourne obtained!")
                print(crafted(legendary_item_materials, material))
                done = True
                break

        elif material == "fragments":
            legendary_item_materials["fragments"] += quantity
            if legendary_item_materials["fragments"] >= 250:
                print("Valanyr obtained!")
                print(crafted(legendary_item_materials, material))
                done = True
                break

        elif material == "motes":
            legendary_item_materials["motes"] += quantity
            if legendary_item_materials["motes"] >= 250:
                print("Dragonwrath obtained!")
                print(crafted(legendary_item_materials, material))
                done = True
                break
        else:
            if material not in legendary_item_materials:
                legendary_item_materials[material] = 0
            legendary_item_materials[material] += quantity
