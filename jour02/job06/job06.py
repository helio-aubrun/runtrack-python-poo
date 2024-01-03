class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "En cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Plat '{nom_plat}' déjà présent dans la commande.")

    def annuler_commande(self):
        self.__statut_commande = "Annulée"
        print("Commande annulée.")

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values() if plat["statut"] == "En cours")
        return total

    def afficher_commande(self):
        print(f"\nCommande N°{self.__numero_commande}")
        for nom_plat, plat_info in self.__plats_commandes.items():
            print(f"{nom_plat}: {plat_info['prix']} € ({plat_info['statut']})")
        total = self.__calculer_total()
        print(f"\nTotal à payer : {total} €")
        print(f"Statut de la commande : {self.__statut_commande}")

    def calculer_tva(self):
        total = self.__calculer_total()
        tva = 0.2 * total
        return tva

commande1 = Commande(numero_commande=1)
commande1.ajouter_plat("Pizza", 12.5)
commande1.ajouter_plat("Salade", 8.0)
commande1.ajouter_plat("Pizza", 12.5)
commande1.afficher_commande()
tva_commande1 = commande1.calculer_tva()
print(f"TVA à payer pour la commande : {tva_commande1} €")
commande1.annuler_commande()
commande1.afficher_commande()