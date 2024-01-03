class Livre():

    def __init__(self,title, aut, page):
        self.__title = title
        self.__aut = aut
        self.__page = page
        self.__disponible = True

    def get_title(self):
        return self.__title

    def get_aut(self):
        return self.__aut
    
    def get_page(self):
        return self.__page
    
    def set_title(self,var):
        self.__title = var

    def set_aut(self,var):
        self.__aut = var

    def set_page(self,var):
        if var % 1 == 0:
            self.__page = var
        else:
            print ("Erreur inserez un nombre entier")

    def get_verification(self):
        if self.__disponible:
            return True
        else:
            return False
    
    def set_emprunter(self):
        if self.get_verification():
            self.__disponible = False
        else:
            print ("livre déjà emprunté")
        
    def set_rendre(self):
        if not self.get_verification():
            self.__disponible = True
        else:
            print ("livre déjà rendu")
        
livre = Livre("LOTR","Tolkien", 722 )
print (livre.get_title())
print (livre.get_aut())
print (livre.get_page())
livre.set_title("Henry potdebeurre")
livre.set_aut("Rowling")
livre.set_page(26.2)
livre.set_page(305)
print (livre.get_title())
print (livre.get_aut())
print (livre.get_page())