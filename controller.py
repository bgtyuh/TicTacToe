class TicTacToeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.score_o = 0
        self.score_x = 0

    def handle_click(self, row, col):
        """Gère le clic d'un joueur ou de l'ordinateur"""
        if not self.model.play_turn(row, col):
            return  # Ne fait rien si la case est déjà prise

        # Met à jour l'affichage du bouton avec le symbole du joueur
        player_symbol = "O" if self.model.current_player == -1 else "X"
        self.view.update_button(row, col, player_symbol)

        # Vérifie si un joueur a gagné
        if self.model.check_winner(row, col):
            if self.model.current_player == -1:
                self.score_o += 1
            else:
                self.score_x += 1
            self.view.update_scores(self.score_o, self.score_x)
            self.view.display_winner(-self.model.current_player)
            self.reset_game()
        elif self.model.is_draw():
            self.view.display_draw()
            self.reset_game()

    def reset_game(self):
        """Réinitialise le jeu"""
        self.model.reset()
        self.view.reset_grid()
