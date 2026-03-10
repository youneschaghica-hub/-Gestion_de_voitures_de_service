class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
        print(f"Employé : {self.nom} {self.prenom}, numéro Permis : {self.numeroPermis}")
        if self.voitureService:
            print("Voiture attribuée :")
            self.voitureService.afficherInformations()
        else:
            print("Aucune voiture attribuée.")

    def affecterVoiture(self, voiture):
        if voiture.chauffeur is not None:
            print(f"Erreur : la voiture {voiture.matricule} est déjà attribuée à {voiture.chauffeur.nom}.")
        else:
            if self.voitureService:
                print(f"Attention : l'employé {self.nom} avait déjà une voiture, elle sera remplacée.")
                self.voitureService.chauffeur = None
            self.voitureService = voiture
            voiture.chauffeur = self

    def retirerVoiture(self):
        if self.voitureService:
            self.voitureService.chauffeur = None
            self.voitureService = None
        else:
            print(f"{self.nom} n'a pas de voiture à retirer.")