from client import Client
from employe import Employe
from enseignant import Enseignant
from etudiant import Etudiant

# Class principal

class Personne :

    #Intanciation de la classe Employe
    employe1 = Employe("Alpha Bah", 35, 5000)
    employe1.augmenter_salaire(10)
    employe1.affiche_informations()

    #Intanciation de la classe Etudiant
    etudiant1 = Etudiant("Josephine Baker", 20, "Programmation C")
    etudiant1.change_matiere_preferee("Developpement Python")
    etudiant1.affiche_informations()

    #Intanciation de la classe Enseignant
    enseignant1 = Enseignant("Yohann Amar", 50, ["Langage C", "Python"])
    enseignant1.ajout_matiere_enseignee("Science Politique")
    enseignant1.affiche_informations()

client = []

client.append(Client("Oumar Tall", 74))
client[0].ajout_commande("25")
client.append(Client("Alpha BAH", 15))
client[1].ajout_commande("70")

for client in client:
    client.affiche_commandes()
