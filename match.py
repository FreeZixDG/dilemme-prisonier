from round import Round
from joueur import Joueur

class Match:
    def __init__(self, joueur1, joueur2, nb_rounds):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.nb_rounds = nb_rounds
        self.historique_joueur1 = []  # Historique vu par joueur1 (adversaire en premier)
        self.historique_joueur2 = []  # Historique vu par joueur2 (adversaire en premier)

    def jouer(self):
        for _ in range(self.nb_rounds):
            round = Round(self.joueur1, self.joueur2, self.historique_joueur1, self.historique_joueur2)
            round.jouer()
