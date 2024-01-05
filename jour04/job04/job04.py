class Forme:

    def aire(self):
        return 0

class Rectangle(Forme):
    
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

rectangle1 = Rectangle(largeur=5, hauteur=3)
print("Aire du rectangle :", rectangle1.aire())