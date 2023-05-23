from contextlib import nullcontext


class Client:
    
    compteur  = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.commandes = []
        Client.compteur += 1
        self.numero_client = Client.compteur

    def ajout_commande(self, commande):
        self.commandes.append(commande)

    def affiche_commandes(self):
        print("******** Liste des Clients ************: ")
        print("Infos du Client : ", self.numero_client)

        if len(self.commandes) == 0:
            print("Aucune commande pour ce client.")
        else:
            
            print("Nom du client : " + self.nom + ":")
            for commande in self.commandes:
                print("- Numero de la Commande :", commande)
        print("********************: ")
