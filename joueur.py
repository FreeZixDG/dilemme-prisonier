from strat import Strat

class Joueur:
    def __init__(self, nom, strategie: Strat):
        self.nom = nom
        self.strategie = strategie
        self.score = 0

    def jouer(self, adversaire):
        return self.strategie.decider(adversaire)
