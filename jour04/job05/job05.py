import math
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
        return math.pi * self.radius ** 2

rectangle1 = Rectangle(largeur=5, hauteur=3)
print("Aire du rectangle :", rectangle1.aire())
cercle1 = Cercle(radius=4)
print("Aire du cercle :", cercle1.aire())