class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Valeur de x : {self.x}")

    def afficherY(self):
        print(f"Valeur de y : {self.y}")

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur

# Instanciation d'un point
point1 = Point(9, 17)

# Affichage des coordonnées initiales
point1.afficherLesPoints()

# Affichage des valeurs de x et y
point1.afficherX()
point1.afficherY()

# Modification des valeurs de x et y
point1.changerX(12)
point1.changerY(9)

# Affichage des nouvelles coordonnées
point1.afficherLesPoints()
