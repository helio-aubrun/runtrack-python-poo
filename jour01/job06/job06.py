class animal():

    def __init__(self):
        self.nom=""
        self.age=0

    def vieillir(self):
        self.age+=1
        if self.age == 1:
            print("L'age de l'animal",self.age,"an")
        else:
            print("L'age de l'animal",self.age,"ans")
    
    def nommer(self,nom):
        self.nom=nom
        print ("L'animal se nomme",self.nom)
    
luna=animal()
luna.vieillir()
luna.vieillir()
luna.nommer("Luna")