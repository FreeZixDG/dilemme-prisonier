from match import Match
from joueur import Joueur
import numpy as np

class Tournoi:
    def __init__(self, strategies, nb_matchs=5, nb_rounds=100):
        self.strategies = strategies
        self.nb_matchs = nb_matchs
        self.nb_rounds = nb_rounds
        self.resultats = {strategie: {'scores': [], 'variance': []} for strategie in strategies}
        self.match_details = []

    def jouer(self):
        for i, strat1 in enumerate(self.strategies):
            for j, strat2 in enumerate(self.strategies):

                for _ in range(self.nb_matchs):
                    match = Match(Joueur("A", strat1), Joueur("B", strat2), self.nb_rounds)
                    match.jouer()
                    # Collecte des résultats de chaque match
                    self.match_details.append({
                        'strat1': strat1.__class__.__name__,
                        'strat2': strat2.__class__.__name__,
                        'scores': (match.joueur1.score, match.joueur2.score),
                        'historique': match.historique_joueur1
                    })
                    # Stockage des scores
                    self.resultats[strat1]['scores'].append(match.joueur1.score)
                    self.resultats[strat2]['scores'].append(match.joueur2.score)

        # Calcul des variances des scores pour chaque stratégie
        for strategie, data in self.resultats.items():
            data['variance'] = np.var(data['scores'])

    def show_results(self):
        # Affichage des détails des matchs
        print("Détails des matchs:")
        for detail in self.match_details:
            print(f"\nMatch entre {detail['strat1']} et {detail['strat2']}:")
            print(f"Scores: {detail['scores']}")
            # print(f"Historique des choix: {detail['historique']}")

        print("\nStatistiques des stratégies:")
        for strategie, data in self.resultats.items():
            moyenne = np.mean(data['scores'])
            variance = data['variance']
            print(f"\nStratégie {strategie.__class__.__name__}:")
            print(f"  Moyenne des scores: {moyenne:.2f}")
            print(f"  Variance des scores: {variance:.2f}")
            print(f"  Scores obtenus: {data['scores']}")
