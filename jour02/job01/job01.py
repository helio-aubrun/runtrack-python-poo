class Rectangle():

    def __init__(self,long,larg):
        self.__long=long
        self.__larg=larg

    def get_larg(self):
        return self.__larg
    
    def get_long(self):
        return self.__long
    
    def set_larg(self,larg):
        self.__larg = larg

    def set_long(self,long):
        self.__long = long

rec = Rectangle(10,5)
print (rec.get_long())
print (rec.get_larg())
rec.set_long(20)
rec.set_larg(10)
print (rec.get_long())
print (rec.get_larg())