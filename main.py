from model import TicTacToeModel
from view import TicTacToeView
from controller import TicTacToeController


def main():
    n = 3  # Taille de la grille
    model = TicTacToeModel(n)

    # Créer le contrôleur
    controller = TicTacToeController(model, None)  # Initialisation avec "None" pour la vue temporairement

    # Créer la vue et l'associer au contrôleur
    view = TicTacToeView(controller, n)

    # Assigner la vue au contrôleur après sa création
    controller.view = view

    # Démarrer la boucle principale de Tkinter
    view.start()


if __name__ == "__main__":
    main()
