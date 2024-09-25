import random

from model import TicTacToeModel


class TicTacToeController:
    def __init__(self):
        self.model = None
        self.view = None
        self.score_o = 0
        self.score_x = 0
        self.opponent_type = "human"  # Défaut : jouer contre un humain

    def start_game(self, grid_size, opponent_type):
        """Démarre le jeu avec la taille de la grille et l'adversaire choisis"""
        self.opponent_type = opponent_type
        self.model = TicTacToeModel(grid_size)
        self.view.create_game_window(grid_size, opponent_type)

    def handle_click(self, row, col):
        """Gère le clic du joueur"""
        if not self.model.play_turn(row, col):
            return

        player_symbol = "O" if self.model.current_player == -1 else "X"
        self.view.update_button(row, col, player_symbol)

        if self.model.check_winner(row, col):
            if self.model.current_player == -1:
                self.score_o += 1
            else:
                self.score_x += 1
            self.view.update_scores(self.score_o, self.score_x)
            self.view.display_winner(-self.model.current_player)
            self.reset_game(self.model.n)
        elif self.model.is_draw():
            self.view.display_draw()
            self.reset_game(self.model.n)

        if self.opponent_type == "computer" and self.model.current_player == -1:
            self.computer_turn() # L'oridnateur joue

    def computer_turn(self):
        """L'ordinateur joue un coup aléatoire"""
        available_moves = [
            (i, j) for i in range(self.model.n) for j in range(self.model.n)
            if self.model.grid[i][j] == 0
        ]

        if available_moves:
            row, col = random.choice(available_moves)  # Choisit un coup au hasard
            self.model.play_turn(row, col)  # Joue le coup dans le modèle
            self.view.update_button(row, col, "X")  # Met à jour la grille avec le symbole "O"

            # Vérifie si l'ordinateur a gagné
            if self.model.check_winner(row, col):
                self.score_x += 1
                self.view.update_scores(self.score_o, self.score_x)
                self.view.display_winner(-1)
                self.reset_game(self.model.n)
            elif self.model.is_draw():
                self.view.display_draw()
                self.reset_game(self.model.n)

    def reset_game(self, grid_size):
        """Réinitialise la grille et les scores"""
        self.model.reset()
        self.view.reset_grid(grid_size)
