class Personne():
    
    def __init__(self, nom, prenom):
        self.prenom=prenom
        self.nom=nom

    def SePresenter(self):
        print ("je suis",self.prenom, self.nom)

John=Personne("Doe","John")
Jean=Personne("Dupond", "Jean")
John.SePresenter()
Jean.SePresenter()