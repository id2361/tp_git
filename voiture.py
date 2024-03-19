class Voiture:
    def __init__(self, nom, couleur):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
  
    def accelere(self, increment):
        if increment > 10:
            increment = 10
            self.vitesse = min(130, self.vitesse + increment)