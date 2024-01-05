class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):

    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self,longueur, largeur)
        self.__hauteur = hauteur
        self.__longueur = longueur
        self.__largeur = largeur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur

rectangle1 = Rectangle(longueur=5, largeur=3)
print("Périmètre du rectangle :", rectangle1.perimetre())
print("Surface du rectangle :", rectangle1.surface())
rectangle1.set_longueur(8)
rectangle1.set_largeur(4)
print("Nouvelle longueur du rectangle :", rectangle1.get_longueur())
print("Nouvelle largeur du rectangle :", rectangle1.get_largeur())
parallelepipede1 = Parallelepipede(longueur=3, largeur=2, hauteur=4)
print("Volume du parallélépipède :", parallelepipede1.volume())