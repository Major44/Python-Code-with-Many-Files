
class Etudiant:
    def __init__(self, nom, age, matiere_preferee):
        self.nom = nom
        self.age = age
        self.matiere_preferee = matiere_preferee

    def change_matiere_preferee(self, nouvelle_matiere):
        self.matiere_preferee = nouvelle_matiere

    def affiche_informations(self):
        print("L'etudiant est :")
        print("Nom:", self.nom)
        print("Age:", self.age)
        print("Matiere preferee:", self.matiere_preferee)
        print("******************\n")
