import tkinter as tk
from tkinter import messagebox

class TicTacToeView:
    def __init__(self, controller, n=3):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Création de la grille
        self.buttons = [[None for _ in range(n)] for _ in range(n)]
        self.n = n
        self.create_grid()

        # Ajout des labels pour afficher les scores
        self.score_label_o = tk.Label(self.window, text="Player O: 0")
        self.score_label_o.grid(row=n, column=0, columnspan=n//2)

        self.score_label_x = tk.Label(self.window, text="Player X: 0")
        self.score_label_x.grid(row=n, column=n//2, columnspan=n//2)

    def start(self):
        """Démarre la boucle principale Tkinter après l'initialisation complète"""
        self.window.mainloop()

    def create_grid(self):
        """Création des boutons pour représenter la grille de jeu"""
        for i in range(self.n):
            for j in range(self.n):
                button = tk.Button(self.window, text="", width=10, height=3,
                                   command=lambda i=i, j=j: self.controller.handle_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def update_button(self, row, col, player_symbol):
        """Met à jour le texte du bouton selon le symbole du joueur (O ou X)"""
        self.buttons[row][col].config(text=player_symbol)

    def display_winner(self, player):
        """Affiche un message de victoire et propose de rejouer"""
        winner = "O" if player == 1 else "X"
        messagebox.showinfo("Winner", f"Player {winner} wins!")
        self.reset_grid()

    def display_draw(self):
        """Affiche un message de match nul et propose de rejouer"""
        messagebox.showinfo("Draw", "It's a draw!")
        self.reset_grid()

    def reset_grid(self):
        """Réinitialise la grille pour une nouvelle partie"""
        for i in range(self.n):
            for j in range(self.n):
                self.buttons[i][j].config(text="")

    def update_scores(self, score_o, score_x):
        """Mise à jour des scores des joueurs"""
        self.score_label_o.config(text=f"Player O: {score_o}")
        self.score_label_x.config(text=f"Player X: {score_x}")
