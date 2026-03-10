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

class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
        print(f"Voiture : {self.marque} ({self.annee}), Matricule : {self.matricule}, Kilométrage : {self.kilometrage}")
        if self.chauffeur:
            print(f"Attribuée à : {self.chauffeur.nom} {self.chauffeur.prenom}")
        else:
            print("Pas attribuée à un employé.")
v1 = Voiture("AB-123-CD", 2015, "jeep", 130000)
v2 = Voiture("EF-456-GH", 2018, "Audi", 50000)
v3 = Voiture("IJ-789-KL", 2022, "GMC", 90000)

e1 = Employe("P123456", "alex", "batna ")
e2 = Employe("P654321", "dihia", "Alice")
e3 = Employe("P987654", "francis", "lookman")

for e in [e1, e2, e3]:
    e.afficherInformations()

for v in [v1, v2, v3]:
    v.afficherInformations()
e1.affecterVoiture(v1)
e2.affecterVoiture(v2)
e3.affecterVoiture(v3)

print("Après affectation des voitures :")
for e in [e1, e2, e3]:
    e.afficherInformations()
e2.retirerVoiture()
print("Après retrait de la voiture de dihia :")
e2.afficherInformations()
