class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculer_prix_ttc(self):
        prix_ttc = self.prixHT * (1 + self.TVA / 100)
        return prix_ttc

    def afficher(self):
        infos_produit = f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%"
        return infos_produit

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenir_nom(self):
        return self.nom

    def obtenir_prix(self):
        return self.prixHT

    def obtenir_tva(self):
        return self.TVA

produit1 = Produit("Saumon", 50, 20)
produit2 = Produit("Fois gras", 30, 10)
print(produit1.afficher())
print(produit2.afficher())
prix_ttc_produit1 = produit1.calculer_prix_ttc()
prix_ttc_produit2 = produit2.calculer_prix_ttc()
print(f"Prix TTC Produit 1: {prix_ttc_produit1}")
print(f"Prix TTC Produit 2: {prix_ttc_produit2}")
produit1.modifier_nom("Huîtres")
produit1.modifier_prix(60)
produit2.modifier_nom("Chapon")
produit2.modifier_prix(40)
print(produit1.afficher())
print(produit2.afficher())
print(f"Nouveau Prix TTC Produit 1: {produit1.calculer_prix_ttc()}")
print(f"Nouveau Prix TTC Produit 2: {produit2.calculer_prix_ttc()}")