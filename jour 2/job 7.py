# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:38:07 2023

@author: aubru
"""

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"
    
class Jeu:
    def __init__(self):
        self.paquet = []
        for couleur in ["Coeur", "Pique", "Carreau", "Trèfle"]:
            for valeur in range(2, 11):
                self.paquet.append(Carte(valeur, couleur))
            for valeur in ["Valet", "Dame", "Roi"]:
                self.paquet.append(Carte(10, couleur))
            self.paquet.append(Carte(1, couleur))
            self.paquet.append(Carte(11, couleur))
        random.shuffle(self.paquet)
    
    def donner_carte(self):
        return self.paquet.pop()
    
    def valeur_main(self, main):
        total = 0
        as_count = 0
        for carte in main:
            if carte.valeur == "As":
                as_count += 1
            else:
                total += carte.valeur
        for i in range(as_count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total

def main():
    jeu = Jeu()
    main_joueur = []
    main_croupier = []
    main_joueur.append(jeu.donner_carte())
    main_joueur.append(jeu.donner_carte())
    main_croupier.append(jeu.donner_carte())
    main_croupier.append(jeu.donner_carte())
    
    print("Main joueur: ", main_joueur)
    print("Total: ", jeu.valeur_main(main_joueur))
    print("Main croupier: ", [main_croupier[0], "X"])
    
    while True:
        choix = input("Voulez-vous une carte (o/n)? ")
        if choix == "o":
            main_joueur.append(jeu.donner_carte())
            print("Main joueur: ", main_joueur)
            total_joueur = jeu.valeur_main(main_joueur)
            print("Total: ", total_joueur)
            if total_joueur > 21:
                print("Perdu!")
                return
        else:
            break
            
    total_joueur = jeu.valeur_main(main_joueur)
    total_croupier = jeu.valeur_main(main_croupier)
    
    while total_croupier < 17:
        main_croupier.append(jeu.donner_carte())
        total_croupier = jeu.valeur_main(main_croupier)
    
    print("Main croupier: ", main_croupier)
    print("Total croupier: ", total_croupier)
    
    if total_joueur > 21:
        print("Perdu!")
    elif total_croupier > 21:
        print("Gagné!")
    elif total_joueur > total_croupier:
        print("Gagné!")
    elif total_croupier > total_joueur:
        print("Perdu!")
    else:
        print("Match nul!")
        
if __name__ == "__main__":
    main()
