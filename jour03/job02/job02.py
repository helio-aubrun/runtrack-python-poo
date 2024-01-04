class CompteBancaire():

    def __init__(self, num, nom, prenom, solde,decouvert):
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        if decouvert == "oui":
            self.__decouvert = True
        else :
            self.__decouvert = False

    def get_afficher(self):
        print ("Nom :", self.__nom)
        print ("Prenom :", self.__prenom)
        print ("Numero du compte :",self.__num)
    
    def get_afficherSolde(self):
        print ("Solde du client :",self.__solde,"€")
    
    def set_versement(self,montant):
        self.__solde+=montant

    def set_retrait(self,montant):
        if self.__decouvert :
            self.__solde-=montant
        else :
            if self.__solde >= montant:
                self.__solde-=montant
            else :
                print ("Erreur, solde insuffisante")

    def set_agios(self):
        if self.__solde < 0:
            agios = (self.__solde * 15)//100
            self.set_retrait(agios)
            print (agios,"€ d'agios ont été percue")
        
    def set_virement(self,receveur, montant):
        if self.__decouvert:
            self.set_retrait(montant)
            receveur.set_versement(montant)
            print ("Virement effectué")
        elif self.__solde >= montant :
            self.set_retrait(montant)
            receveur.set_versement(montant)
            print ("Virement effectué")
        else :
            print ("Erreur solde insuffisante")

John = CompteBancaire(1004,"Doe","John",1500,"oui")
John.get_afficher()
John.set_versement(1500)
John.set_retrait(5000)
John.set_retrait(1000)
John.get_afficherSolde()
John.set_agios()
John.get_afficherSolde()
Jackie = CompteBancaire(1005,"Welles","Jackie", 5000,"oui")
Jackie.set_virement(John,2550)
Jackie.get_afficherSolde()
John.get_afficherSolde()