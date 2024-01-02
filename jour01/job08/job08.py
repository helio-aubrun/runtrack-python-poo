from math import *
class Cercle():
    def __init__(self,rayon):
        self.rayon=rayon
    
    def ChangerRayon(self,new):
        self.rayon=new
        print ("Le rayon à été modifié")

    def diametre(self):
        return self.rayon*2
    
    def circonférence(self):
        return self.diametre() * pi
    
    def aire(self):
        return pi * (self.rayon*self.rayon)

    def afficherInfos(self):
        print ("Le rayon est de",self.rayon)
        print ("La circonférence est de",round(self.circonférence(),4))
        print ("L'aire est de",round(self.aire(),4))
        print ("Le diametre est de",self.diametre())
    
job08=Cercle(4)
job08.afficherInfos()
job08.ChangerRayon(7)
job08.afficherInfos()