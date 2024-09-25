from model import TicTacToeModel
from view import TicTacToeView
from controller import TicTacToeController


def main():
    # Choisir la taille de la grille
    n = int(input("Choose the size of the grid (e.g., 3 for a 3x3 grid): "))

    # Initialisation du modèle, de la vue et du contrôleur
    model = TicTacToeModel(n)
    view = TicTacToeView()
    controller = TicTacToeController(model, view)

    # Démarrer le jeu
    controller.play_game()


if __name__ == "__main__":
    main()
