# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:16:44 2023

@author: aubru
"""

class Vehicule:
    def __init__(self, marque, annee, prix, modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def informationsVehicule(self):
        print("Marque = ", self.marque)
        print("Modèle = ", self.modele)
        print("Année = ", self.annee)
        print("Prix = ", self.prix)

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, modele, portes=4):
        super().__init__(marque, annee, prix, modele)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, annee, prix, modele, roues=2):
        super().__init__(marque, annee, prix, modele)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print("WEWEWE ! EN Y T A CAPTE !")



ma_voiture = Voiture("Peugeot", 2020, 20000,"Class A")
ma_voiture.informationsVehicule()
ma_moto = Moto("Honda", 2019, 15000,"1200 Vmax")
ma_moto.informationsVehicule()
ma_voiture.demarrer()
ma_moto.demarrer()