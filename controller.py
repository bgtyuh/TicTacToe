import random

class TicTacToeController:
    def __init__(self, model, view):
        self.opponent = None
        self.model = model
        self.view = view
        self.score_o = 0
        self.score_x = 0

    def start_game(self):
        """Démarre la première partie et demande l'adversaire (humain ou ordinateur) une seule fois"""
        # Demande si l'utilisateur joue contre un autre humain ou contre l'ordinateur
        self.opponent = self.view.ask_for_opponent()

        # Lance la première partie
        self.play_game()

    def play_game(self):
        """Démarre une partie"""
        self.model.reset()
        game_over = False

        while not game_over:
            # Efface la console et affiche la grille actuelle
            self.view.clear_console()
            self.view.display_grid(self.model.grid)

            # Vérifie si c'est le tour de l'ordinateur
            if self.model.current_player == -1 and self.opponent == 'c':  # Le joueur 'X' est l'ordinateur
                row, col = self.get_computer_move()  # L'ordinateur joue un coup aléatoire
            else:
                row, col = self.view.get_player_input(self.model.n)  # L'utilisateur joue

            # Joue le coup
            if not self.model.play_turn(row, col):
                print("Position already taken, try again.")
                continue

            # Vérifie si le joueur a gagné
            if self.model.check_winner(row, col):
                self.view.clear_console()
                self.view.display_grid(self.model.grid)
                self.view.display_winner(-self.model.current_player)
                if self.model.current_player == -1:  # Le joueur 'O' a gagné
                    self.score_o += 1
                else:  # Le joueur 'X' a gagné
                    self.score_x += 1
                self.view.display_score(self.score_o, self.score_x)
                game_over = True

            # Vérifie si la partie est nulle
            elif self.model.is_draw():
                self.view.clear_console()
                self.view.display_grid(self.model.grid)
                self.view.display_draw()
                game_over = True

        # Demande si l'utilisateur veut rejouer
        if self.view.ask_for_replay():
            self.play_game()
        else:
            self.display_final_score()

    def get_computer_move(self):
        """Choix aléatoire de l'ordinateur pour une case vide"""
        empty_positions = [(i, j) for i in range(self.model.n) for j in range(self.model.n) if
                           self.model.grid[i][j] == 0]
        return random.choice(empty_positions)

    def display_final_score(self):
        """Affiche le score final lorsque le joueur quitte."""
        self.view.clear_console()
        print("Game Over!")
        if self.score_o > self.score_x:
            print(f"Final Score: Player O wins with {self.score_o} win(s) | Player X: {self.score_x} win(s)")
        elif self.score_x > self.score_o:
            print(f"Final Score: Player X wins with {self.score_x} win(s) | Player O: {self.score_o} win(s)")
        else:
            print(f"Final Score: It's a tie! Both players won {self.score_o} time(s)")
