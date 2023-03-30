# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:04:31 2023

@author: aubru
"""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def retour_longueur(self):
        return self.__longueur

    def modi_longueur(self, longueur):
        self.__longueur = longueur

    def retour_largeur(self):
        return self.__largeur

    def modi_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def retour_hauteur(self):
        return self.__hauteur

    def modi_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

r = Rectangle(5, 10)
print("Longueur : ", r.retour_longueur())
print("Largeur : ", r.retour_largeur())
print("Périmètre : ", r.perimetre())
print("Surface : ", r.surface())
p = Parallelepipede(5, 10, 3)
print("Longueur : ", p.retour_longueur())
print("Largeur : ", p.retour_largeur())
print("Hauteur : ", p.retour_hauteur())
print("Périmètre : ", p.perimetre())
print("Surface : ", p.surface())
print("Volume : ", p.volume())