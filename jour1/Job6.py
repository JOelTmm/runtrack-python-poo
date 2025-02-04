class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation de l'animal
animal = Animal()

# Affichage de l'âge initial de l'animal
print(f"L'age de l'animal {animal.age} ans")

# L'animal vieillit
animal.vieillir()

# Affichage de l'âge après avoir vieilli
print(f"L'age de l'animal {animal.age} ans")

# Nommer l'animal
animal.nommer("Luna")

# Affichage du nom de l'animal
print(f"L'animal se nomme {animal.prenom}")
