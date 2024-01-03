class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, nouvel_etat):
        self.__en_marche = nouvel_etat

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer, le réservoir est trop bas.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    def __verifier_plein(self):
        return self.__reservoir > 5

ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, kilometrage=15000)
print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
ma_voiture.demarrer()
ma_voiture.arreter()