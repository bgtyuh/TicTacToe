from view import TicTacToeView
from controller import TicTacToeController

def main():
    controller = TicTacToeController()
    view = TicTacToeView(controller)
    controller.view = view
    view.start()

if __name__ == "__main__":
    main()
