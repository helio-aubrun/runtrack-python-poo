class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.y -= 1

    def droite(self):
        self.y += 1

    def haut(self):
        self.x -= 1

    def bas(self):
        self.x += 1

    def position(self):
        return (self.x, self.y)

plateau_jeu = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
mon_personnage = Personnage(2, 2)
mon_personnage.droite()
print("Nouvelle position:", mon_personnage.position())
mon_personnage.gauche()
print("Nouvelle position:", mon_personnage.position())
mon_personnage.haut()
print("Nouvelle position:", mon_personnage.position())
mon_personnage.bas()
print("Nouvelle position:", mon_personnage.position())