import os
import platform

class TicTacToeView:
    @staticmethod
    def clear_console():
        """Efface la console pour garder un affichage propre."""
        # Utilisation de la commande clear ou cls selon l'OS
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def display_grid(grid):
        """Affiche la grille dans la console"""
        n = len(grid)
        ch = "\n+"
        ch += "---+" * n
        ch += "\n"
        for line in grid:
            ch += "|"
            for elt in line:
                ch += " "
                if elt == 1:
                    ch += "O"
                elif elt == -1:
                    ch += "X"
                else:
                    ch += " "
                ch += " |"
            ch += "\n+"
            ch += "---+" * n
            ch += "\n"
        print(ch)

    @staticmethod
    def get_player_input(n):
        """Récupère les coordonnées du joueur (ligne, colonne)"""
        while True:
            try:
                row = int(input(f"Chose a line (1-{n}): ")) - 1
                col = int(input(f"Chose a column (1-{n}): ")) - 1
                if 0 <= row < n and 0 <= col < n:
                    return row, col
                else:
                    print(f"Invalid input, please choose between 1 and {n}.")
            except ValueError:
                print("Invalid input, please enter numbers only.")

    @staticmethod
    def display_winner(player):
        """Affiche le gagnant"""
        winner = "O" if player == 1 else "X"
        print(f"Player {winner} wins!")

    @staticmethod
    def display_draw():
        """Affiche le message d'égalité"""
        print("It's a draw!")

    @staticmethod
    def display_score(score_o, score_x):
        """Affiche les scores"""
        print(f"Scores: Player O has {score_o} win(s) | Player X has {score_x} win(s)")

    @staticmethod
    def ask_for_replay():
        """Demande à l'utilisateur s'il veut rejouer"""
        replay = ''
        while replay not in ['y', 'n']:
            replay = input("Do you want to start a new game? (y/n): ").lower()
        return replay == 'y'
