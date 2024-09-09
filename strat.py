import random

from choix import Choix  # Importe l'énumération Choix

class Strat:
    def decider(self, adversaire):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

class Confiance(Strat):
    def decider(self, adversaire):
        return Choix.CONFIANCE

class Triche(Strat):
    def decider(self, adversaire):
        return Choix.TRAHISON

class Copycat(Strat):
    def decider(self, historique):
        if not historique:
            return Choix.CONFIANCE

        dernier_choix_adversaire, _ = historique[-1]
        return dernier_choix_adversaire


class Analyse(Strat):
    def decider(self, historique):
        if not historique:
            return Choix.CONFIANCE

        total_rounds = len(historique)
        trahisons_adversaire = sum(1 for choix_adversaire, _ in historique if choix_adversaire == Choix.TRAHISON)

        if trahisons_adversaire / total_rounds > 0.5:
            return Choix.TRAHISON
        else:
            return Choix.CONFIANCE

class Random(Strat):
    def decider(self, historique):
        return random.choice([c for c in Choix])

class Rancunier(Strat):
    def decider(self, historique):
        if not historique:
            return Choix.CONFIANCE

        adversaire_a_trahit = any(choix_adversaire for choix_adversaire, _ in historique if choix_adversaire == Choix.TRAHISON)
        if adversaire_a_trahit:
            return Choix.TRAHISON
        else:
            return Choix.CONFIANCE

class Chelou(Strat):
    def decider(self, historique):
        if not historique:
            return Choix.CONFIANCE

        return Choix.TRAHISON