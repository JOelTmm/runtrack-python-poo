class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Affichage du résultat en appelant la méthode SePresenter()
print(personne1.SePresenter())
print(personne2.SePresenter())
