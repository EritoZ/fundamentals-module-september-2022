class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {zoo_name}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishes in {zoo_name}: {', '.join(self.fishes)}")
        elif species == "bird":
            print(f"Birds in {zoo_name}: {', '.join(self.birds)}")

        print(f"Total animals: {Zoo.__animals}")


zoo_name = input()
number = int(input())
zoo_class = Zoo(zoo_name)

for i in range(number):
    species, name = input().split()

    zoo_class.add_animal(species, name)

zoo_class.get_info(input())
