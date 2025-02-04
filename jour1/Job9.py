class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        """Retourne le prix TTC (prix HT + TVA)."""
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        """Affiche les informations du produit sous forme de chaîne."""
        return f"Nom : {self.nom}\nPrix HT : {self.prixHT} €\nTVA : {self.TVA}%\nPrix TTC : {self.CalculerPrixTTC()} €"

    def modifierNom(self, nouveau_nom):
        """Modifie le nom du produit."""
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prixHT):
        """Modifie le prix HT du produit."""
        self.prixHT = nouveau_prixHT

    def getNom(self):
        """Retourne le nom du produit."""
        return self.nom

    def getPrixHT(self):
        """Retourne le prix HT du produit."""
        return self.prixHT

    def getTVA(self):
        """Retourne la TVA du produit."""
        return self.TVA

    def getPrixTTC(self):
        """Retourne le prix TTC du produit."""
        return self.CalculerPrixTTC()


# Création de plusieurs produits
produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 200, 15)

# Affichage des informations des produits
produit1.afficher()
produit2.afficher()

# Modification du nom et du prix des produits
produit1.modifierNom("Produit A modifié")
produit1.modifierPrix(120)

produit2.modifierNom("Produit B modifié")
produit2.modifierPrix(180)

# Affichage des nouveaux prix des produits
print("Nouveaux produits:")
print(produit1.afficher())
print(produit2.afficher())

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        """Retourne le prix TTC (prix HT + TVA)."""
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        """Affiche les informations du produit sous forme de chaîne."""
        return f"Nom : {self.nom}\nPrix HT : {self.prixHT} €\nTVA : {self.TVA}%\nPrix TTC : {self.CalculerPrixTTC()} €"

    def modifierNom(self, nouveau_nom):
        """Modifie le nom du produit."""
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prixHT):
        """Modifie le prix HT du produit."""
        self.prixHT = nouveau_prixHT

    def getNom(self):
        """Retourne le nom du produit."""
        return self.nom

    def getPrixHT(self):
        """Retourne le prix HT du produit."""
        return self.prixHT

    def getTVA(self):
        """Retourne la TVA du produit."""
        return self.TVA

    def getPrixTTC(self):
        """Retourne le prix TTC du produit."""
        return self.CalculerPrixTTC()


# Création de plusieurs produits
produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 200, 15)

# Affichage des informations des produits
produit1.afficher()
produit2.afficher()

# Modification du nom et du prix des produits
produit1.modifierNom("Pokémon")
produit1.modifierPrix(120)

produit2.modifierNom("LaMano")
produit2.modifierPrix(180)

# Affichage des nouveaux prix des produits
print("Nouveaux produits:")
print(produit1.afficher())
print(produit2.afficher())

