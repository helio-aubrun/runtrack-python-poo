class point():

    def __init__(self,x, y):
        self.x=x
        self.y=y
    
    def afficherLesPoints(self):
        print ("Les coordonnées du point est",self.x,self.y)
    
    def afficherX(self):
        print ("Le point a pour x",self.x)

    def afficherY(self):
        print ("Le point a pour y",self.y)
    
    def changerX(self,new):
        self.x=new
        print ("x a été changé")
    
    def changerY(self,new):
        self.y=new
        print ("y a été changé")
    
job05=point(15,20)
job05.afficherLesPoints()
job05.changerX(20)
job05.changerY(25)
job05.afficherX()
job05.afficherY()