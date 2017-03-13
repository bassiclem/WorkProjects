class Market:
    def __init__(self):
        self.Enseigne ="Monoprix"
        self.Ville = "Paris"
        self.Produit = "alimentation"
        self.Revenu = 1000

    def changer_enseigne(self,nouvelle_enseigne):
        self.Enseigne = nouvelle_enseigne

    def changer_ville(self, nouvelle_ville):
        self.Ville = nouvelle_ville

    def __add__(self, other):
        nouveau_magasin = Market()
        nouveau_magasin.Revenu = self.Revenu
        nouveau_magasin.Revenu += other.Revenu
        nouveau_magasin.Enseigne = nouveau_magasin.Enseigne + " et " + other.Enseigne
        return nouveau_magasin


