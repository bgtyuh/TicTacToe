class TicTacToeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.score_o = 0
        self.score_x = 0

    def play_game(self):
        """Démarre une nouvelle partie"""
        self.model.reset()
        game_over = False

        while not game_over:
            # Efface la console à chaque tour pour garder la trace propre
            self.view.clear_console()

            # Affiche la grille actuelle
            self.view.display_grid(self.model.grid)

            # Affiche les scores
            self.view.display_score(self.score_o, self.score_x)

            # Récupère le coup du joueur
            row, col = self.view.get_player_input(self.model.n)

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
