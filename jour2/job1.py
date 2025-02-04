class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé
        self.__largeur = largeur    # Attribut privé

    # Accesseur pour la longueur
    def getLongueur(self):
        return self.__longueur

    # Mutateur pour la longueur
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    # Accesseur pour la largeur
    def getLargeur(self):
        return self.__largeur

    # Mutateur pour la largeur
    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    # Méthode pour afficher les informations du rectangle
    def afficher(self):
        return f"Longueur : {self.__longueur}, Largeur : {self.__largeur}"

# Instanciation du rectangle avec longueur 10 et largeur 5
rectangle = Rectangle(10, 5)

# Affichage des dimensions initiales
print("Dimensions initiales :", rectangle.afficher())

# Modification de la longueur et de la largeur
rectangle.setLongueur(12)
rectangle.setLargeur(6)

# Vérification des nouvelles dimensions
print("Nouvelles dimensions après modification :", rectangle.afficher())
