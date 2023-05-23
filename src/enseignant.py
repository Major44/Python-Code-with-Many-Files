
class Enseignant:
    def __init__(self, nom, age, matieres_enseignees):
        self.nom = nom
        self.age = age
        self.matieres_enseignees = matieres_enseignees

    def ajout_matiere_enseignee(self, matiere):
        self.matieres_enseignees.append(matiere)

    def affiche_informations(self):
        print("L'enseignant est :")
        print("Nom:", self.nom)
        print("Age:", self.age)
        print("Matieres enseignees:", self.matieres_enseignees)
        print("******************\n")

