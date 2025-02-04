class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Instanciation du personnage
personnage = Personnage(2, 3)

# Affichage de la position initiale
print("Position initiale:", personnage.position())

# Déplacement du personnage
personnage.gauche()
personnage.haut()

# Affichage de la nouvelle position
print("Nouvelle position:", personnage.position())

# Déplacement du personnage à droite et bas
personnage.droite()
personnage.bas()

# Affichage de la position finale
print("Position finale:", personnage.position())
