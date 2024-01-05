import random

class Carte:
    
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:

    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_points(self, main):
        total_points = 0
        nombre_as = 0
        for carte in main:
            if carte.valeur.isdigit():
                total_points += int(carte.valeur)
            elif carte.valeur in ['J', 'Q', 'K']:
                total_points += 10
            elif carte.valeur == 'A':
                total_points += 11
                nombre_as += 1
        while total_points > 21 and nombre_as:
            total_points -= 10
            nombre_as -= 1
        return total_points

    def afficher_main(self, main):
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer(self):
        main_joueur = [self.paquet.pop(), self.paquet.pop()]
        main_croupier = [self.paquet.pop(), self.paquet.pop()]
        while True:
            print("\nMain du joueur :")
            self.afficher_main(main_joueur)
            points_joueur = self.calculer_points(main_joueur)
            print(f"Total des points du joueur : {points_joueur}")
            if points_joueur == 21:
                print("Blackjack ! Vous gagnez !")
                break
            elif points_joueur > 21:
                print("Vous avez dépassé 21. Vous perdez.")
                break
            choix = input("Voulez-vous prendre une carte supplémentaire ? (oui/non) ").lower()
            if choix == 'oui':
                nouvelle_carte = self.paquet.pop()
                print(f"Vous avez pioché un {nouvelle_carte.valeur} de {nouvelle_carte.couleur}.")
                main_joueur.append(nouvelle_carte)
            else:
                break
        while self.calculer_points(main_croupier) < 17:
            nouvelle_carte = self.paquet.pop()
            main_croupier.append(nouvelle_carte)
        print("\nMain du croupier :")
        self.afficher_main(main_croupier)
        points_croupier = self.calculer_points(main_croupier)
        print(f"Total des points du croupier : {points_croupier}")
        if points_joueur > points_croupier or points_croupier > 21:
            print("Vous gagnez !")
        elif points_joueur < points_croupier:
            print("Le croupier gagne.")
        else:
            print("Égalité.")

jeu = Jeu()
jeu.jouer()
