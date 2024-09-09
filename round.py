from choix import Choix

class Round:
    def __init__(self, joueur1, joueur2, historique_joueur1, historique_joueur2):
        """
        historique_joueur1 : liste des tuples (choix_joueur2, choix_joueur1) pour joueur1
        historique_joueur2 : liste des tuples (choix_joueur1, choix_joueur2) pour joueur2
        """
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.historique_joueur1 = historique_joueur1  # Ce que joueur1 voit
        self.historique_joueur2 = historique_joueur2  # Ce que joueur2 voit

    def jouer(self):
        decision1 = self.joueur1.jouer(self.historique_joueur1)
        decision2 = self.joueur2.jouer(self.historique_joueur2)

        self.historique_joueur1.append((decision2, decision1))
        self.historique_joueur2.append((decision1, decision2))

        if decision1 == Choix.CONFIANCE and decision2 == Choix.CONFIANCE:
            self.joueur1.score += 1
            self.joueur2.score += 1
        elif decision1 == Choix.TRAHISON and decision2 == Choix.CONFIANCE:
            self.joueur1.score += 2
            self.joueur2.score -= 2
        elif decision1 == Choix.CONFIANCE and decision2 == Choix.TRAHISON:
            self.joueur2.score += 2
            self.joueur1.score -= 2


