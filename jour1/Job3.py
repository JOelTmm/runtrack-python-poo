class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est", resultat)

# Instanciation de la classe
operation1 = Operation()

# Appel de la méthode addition
operation1.addition()
