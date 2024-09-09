from joueur import Joueur
from strat import *
from tournoi import Tournoi

def main():
    joueur1 = Joueur("Alice", Confiance())
    joueur2 = Joueur("Bob", Triche())
    joueur3 = Joueur("Charlie", Copycat())
    joueur4 = Joueur("Dani",Analyse())

    tournoi = Tournoi([Confiance(), Analyse(), Triche(), Copycat(), Random(), Rancunier(), Chelou()])
    tournoi.jouer()
    tournoi.show_results()

if __name__ == "__main__":
    main()



