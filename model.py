class TicTacToeModel:
    def __init__(self, n):
        self.n = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.current_player = 1  # 1 for O, -1 for X
        self.moves = 0

    def play_turn(self, row, col):
        """Jouer un tour en fonction des coordonnées (row, col)"""
        if self.grid[row][col] == 0:
            self.grid[row][col] = self.current_player
            self.current_player *= -1
            self.moves += 1
            return True
        return False

    def check_winner(self, row, col):
        """Vérifie s'il y a un gagnant après le coup joué"""
        n = self.n
        current_player = -self.current_player  # Le joueur actuel après avoir changé

        # Vérification de la ligne et de la colonne
        if abs(sum(self.grid[row])) == n or abs(sum(self.grid[i][col] for i in range(n))) == n:
            return True

        # Vérification des diagonales
        if row == col and abs(sum(self.grid[i][i] for i in range(n))) == n:
            return True

        if row + col == n - 1 and abs(sum(self.grid[i][n - i - 1] for i in range(n))) == n:
            return True

        return False

    def is_draw(self):
        """Vérifie si la partie est nulle"""
        return self.moves == self.n ** 2

    def reset(self):
        """Réinitialise la grille pour une nouvelle partie"""
        self.grid = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.current_player = 1
        self.moves = 0
