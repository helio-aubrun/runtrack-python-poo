import random

class Personnage:
    
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:

    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancer_jeu(self):
        self.choisir_niveau()
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 70
        elif self.niveau == 3:
            vie_joueur = 60
            vie_ennemi = 90
        else:
            print("Niveau invalide. Le jeu se lance avec le niveau par défaut.")
            vie_joueur = 100
            vie_ennemi = 50
        joueur = Personnage("Ryu", vie_joueur)
        ennemi = Personnage("Akuma", vie_ennemi)
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu. Vous avez gagné!")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu. Vous avez perdu.")
                break
            print(f"{joueur.nom}: Vie = {joueur.vie} | {ennemi.nom}: Vie = {ennemi.vie}")

jeu = Jeu()
jeu.lancer_jeu()