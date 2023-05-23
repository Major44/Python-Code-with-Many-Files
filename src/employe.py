
class Employe:
    def __init__(self, nom, age, salaire):
        self.nom = nom
        self.age = age
        self.salaire = salaire

    def augmenter_salaire(self, pourcentage):
        self.salaire *= (1 + pourcentage / 100)

    def affiche_informations(self):
        print("L'employe est :")
        print("Nom:", self.nom)
        print("Age:", self.age)
        print("Salaire : ", self.salaire)
        print("******************\n")