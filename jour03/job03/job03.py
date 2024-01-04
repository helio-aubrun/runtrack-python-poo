class Tache:

    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - {self.statut}"

class ListeDeTaches:

    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                return f"Tâche '{titre}' supprimée avec succès."
        return f"Tâche '{titre}' non trouvée."

    def marquer_comme_finie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                return f"Tâche '{titre}' marquée comme terminée."
        return f"Tâche '{titre}' non trouvée."

    def afficher_liste(self):
        return [str(tache) for tache in self.taches]

    def filter_liste(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

tache1 = Tache("Cyberpunk", "Finir Cyberpunk 2077")
tache2 = Tache("Linkedin", "Mettre à jour mon Linkedin")
tache3 = Tache("Planète des singes", "Lire le livre La Planète des singes qui traîne depuis 4 mois à côté de mon lit")
liste_taches = ListeDeTaches()
liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)
print("Liste initiale:")
print(liste_taches.afficher_liste())
print("\nSuppression d'une tâche:")
print(liste_taches.supprimer_tache("Cyberpunk"))
print("\nMarquage d'une tâche comme terminée:")
print(liste_taches.marquer_comme_finie("Linkedin"))
print("\nListe mise à jour:")
print(liste_taches.afficher_liste())
print("\nTâches à faire:")
print(liste_taches.filter_liste("À faire"))