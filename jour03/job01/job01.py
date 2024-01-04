class Ville:

    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def set_nombre_habitants(self, nouveau_nombre):
        self.__nombre_habitants = nouveau_nombre

class Personne:
    
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        nouveau_nombre = self.__ville.get_nombre_habitants() + 1
        self.__ville.set_nombre_habitants(nouveau_nombre)

    def afficher_informations(self):
        print(f"{self.__nom}, {self.__age} ans, habitant à {self.__ville.get_nom()}")

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)
print(f"Population de la ville de {paris.get_nom()}: {paris.get_nombre_habitants()} habitants")
print(f"Population de la ville de {marseille.get_nom()}: {marseille.get_nombre_habitants()} habitants")
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()
print(f"Mise a jour de la population de la ville de {paris.get_nom()}  {paris.get_nombre_habitants()} habitants")
print(f"Mise a jour de la population de la ville de {marseille.get_nom()} {marseille.get_nombre_habitants()} habitants")