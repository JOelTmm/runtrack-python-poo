class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

# Instanciation de l'animal
animal = Animal()

# Affichage de l'âge initial de l'animal
print(f"L'age de l'animal {animal.age} ans")

# L'animal vieillit
animal.vieillir()

# Affichage de l'âge après avoir vieilli
print(f"L'age de l'animal {animal.age} ans")
