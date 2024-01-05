class Vehicule():

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print ("marque :", self.marque)
        print ("modèle :", self.modele)
        print ("année :", self.annee)
        print ("prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        print ("marque :", self.marque)
        print ("modèle :", self.modele)
        print ("année :", self.annee)
        print ("prix :", self.prix)
        print ("portes :", self.portes)

    def demarrer(self):
        print ("Tut tut")

class Moto(Vehicule):

    def __init__(self, marque, modele, annee, prix, roue=2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        print ("marque :", self.marque)
        print ("modèle :", self.modele)
        print ("année :", self.annee)
        print ("prix :", self.prix)
        print ("roue :", self.roue)

    def demarrer(self):
        print ("En y t'as capté")

vroum = Voiture("Mercedes", "Class A", "2020", "18500")
vroum.informationsVehicule()
vroumvroum = Moto("Yamaha","1200 Vmax","1987","4500")
vroumvroum.informationsVehicule()
vroum.demarrer()
vroumvroum.demarrer()