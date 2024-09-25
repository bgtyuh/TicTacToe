import tkinter as tk
from tkinter import ttk, messagebox


class TicTacToeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - Menu Principal")
        self.window.configure(bg="#2E3440")

        # Menu principal : Configuration du jeu
        self.grid_size = tk.IntVar(value=3)  # Variable pour la taille de la grille
        self.opponent_type = tk.StringVar(value="human")  # Variable pour choisir entre "humain" ou "ordinateur"

        # Titre du menu principal
        self.title_label = tk.Label(self.window, text="Tic Tac Toe", font=("Helvetica", 24, "bold"), bg="#2E3440",
                                    fg="#ECEFF4")
        self.title_label.pack(pady=20)

        # Option pour la taille de la grille
        self.grid_size_label = tk.Label(self.window, text="Choisir la taille de la grille:", font=("Helvetica", 14),
                                        bg="#2E3440", fg="#88C0D0")
        self.grid_size_label.pack(pady=10)
        self.grid_size_selector = ttk.Combobox(self.window, textvariable=self.grid_size, values=[3, 4, 5],
                                               font=("Helvetica", 12))
        self.grid_size_selector.pack(pady=5)

        # Option pour choisir l'adversaire
        self.opponent_label = tk.Label(self.window, text="Choisir l'adversaire:", font=("Helvetica", 14), bg="#2E3440",
                                       fg="#88C0D0")
        self.opponent_label.pack(pady=10)

        # Boutons radio pour choisir l'adversaire
        self.radio_human = tk.Radiobutton(self.window, text="Jouer contre un humain", variable=self.opponent_type,
                                          value="human", font=("Helvetica", 12), bg="#2E3440", fg="#ECEFF4",
                                          selectcolor="#4C566A")
        self.radio_human.pack(pady=5)
        self.radio_computer = tk.Radiobutton(self.window, text="Jouer contre l'ordinateur", variable=self.opponent_type,
                                             value="computer", font=("Helvetica", 12), bg="#2E3440", fg="#ECEFF4",
                                             selectcolor="#4C566A")
        self.radio_computer.pack(pady=5)

        # Bouton pour démarrer le jeu
        self.start_button = tk.Button(self.window, text="Démarrer le jeu", font=("Helvetica", 14, "bold"), bg="#88C0D0",
                                      fg="#2E3440", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        """Démarre le jeu avec les paramètres choisis dans le menu principal"""
        grid_size = self.grid_size.get()  # Taille de la grille
        opponent = self.opponent_type.get()  # Type d'adversaire (humain ou ordinateur)

        # Passe les paramètres au contrôleur et démarre le jeu
        self.controller.start_game(grid_size, opponent)

    def start(self):
        """Démarre la boucle principale Tkinter pour le menu"""
        self.window.mainloop()

    # Cette partie est l'interface du jeu après la configuration
    def create_game_window(self, grid_size, opponent_type):
        """Crée la fenêtre de jeu après la configuration dans le menu principal"""
        # Création d'une nouvelle fenêtre de jeu
        self.window = tk.Toplevel()  # Nouvelle fenêtre pour la grille de jeu
        self.window.title(
            f"Tic Tac Toe - {grid_size}x{grid_size} - {'Vs Ordinateur' if opponent_type == 'computer' else 'Vs Humain'}")
        self.window.configure(bg="#2E3440")

        self.buttons = [[None for _ in range(grid_size)] for _ in range(grid_size)]

        self.title_label = tk.Label(self.window, text="Tic Tac Toe", font=("Helvetica", 24, "bold"), bg="#2E3440",
                                    fg="#ECEFF4")
        self.title_label.grid(row=0, column=0, columnspan=grid_size, pady=(10, 20))

        self.create_grid(grid_size)

        self.score_label_o = tk.Label(self.window, text="Player O: 0", font=("Helvetica", 14), bg="#2E3440",
                                      fg="#88C0D0")
        self.score_label_o.grid(row=grid_size + 1, column=0, columnspan=grid_size // 2)

        self.score_label_x = tk.Label(self.window, text="Player X: 0", font=("Helvetica", 14), bg="#2E3440",
                                      fg="#D08770")
        self.score_label_x.grid(row=grid_size + 1, column=grid_size // 2, columnspan=grid_size // 2)

    def create_grid(self, grid_size):
        """Création des boutons pour représenter la grille du jeu"""
        for i in range(grid_size):
            for j in range(grid_size):
                button = tk.Button(self.window, text="", width=10, height=3, font=("Helvetica", 18, "bold"),
                                   bg="#4C566A", fg="#ECEFF4", activebackground="#88C0D0",
                                   command=lambda i=i, j=j: self.controller.handle_click(i, j))
                button.grid(row=i + 1, column=j, padx=5, pady=5)  # Ajuste l'espacement entre les boutons
                self.buttons[i][j] = button

    def update_button(self, row, col, player_symbol):
        """Met à jour le texte et la couleur des boutons après un clic"""
        if player_symbol == "O":
            self.buttons[row][col].config(text=player_symbol, bg="#88C0D0", fg="#2E3440")
        else:
            self.buttons[row][col].config(text=player_symbol, bg="#D08770", fg="#2E3440")

    def update_scores(self, score_o, score_x):
        """Met à jour les scores"""
        self.score_label_o.config(text=f"Player O: {score_o}")
        self.score_label_x.config(text=f"Player X: {score_x}")

    def display_winner(self, player):
        """Affiche un message de victoire et propose de rejouer"""
        winner = "O" if player == 1 else "X"
        messagebox.showinfo("Winner", f"Player {winner} wins!")
        self.reset_grid(self.controller.model.n)

    def display_draw(self):
        """Affiche un message de match nul et propose de rejouer"""
        messagebox.showinfo("Draw", "It's a draw!")
        self.reset_grid(self.controller.model.n)

    def reset_grid(self, grid_size):
        """Réinitialise la grille pour une nouvelle partie"""
        for i in range(grid_size):
            for j in range(grid_size):
                self.buttons[i][j].config(text="", bg="#4C566A", fg="#ECEFF4")
