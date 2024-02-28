from bataille import *

def main():
    # Création des joueurs
        joueur1 = Joueur("Joueur 1")
        joueur2 = Joueur("Joueur 2")

    # Création de la partie et démarrage du jeu
        partie = Partie(joueur1, joueur2)
        partie.jouer()
    
if __name__ == "__main__":
      main()

      