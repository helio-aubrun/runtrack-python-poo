# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:09:21 2023

@author: aubru
"""

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return 3.14 * self.radius ** 2

rectangle = Rectangle(5, 10)
print(rectangle.aire())
cercle = Cercle(3)
print(cercle.aire())
