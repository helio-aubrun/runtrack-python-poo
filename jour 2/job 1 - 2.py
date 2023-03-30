# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:57:10 2023

@author: aubru
"""

class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print(f"J'ai {self.age} ans.")
        
    def bonjour(self):
        print("Hello!")


class Eleve(Personne):
    def __init__(self):
        super().__init__()
        
    def allerEnCours(self):
        print("Je vais en cours.")
        
    def affichageAge(self):
        print(f"J'ai {self.age} ans.")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__(age=40)
        self.matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer.")


eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.age = 15
eleve.affichageAge()
professeur = Professeur("mathématiques")
professeur.bonjour()
professeur.enseigner()