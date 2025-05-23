class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'  # Player X starts
        self.winner = None

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None

    def make_move(self, position):
        if self.board[position] == ' ' and self.winner is None:
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)              # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board and self.winner is None

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def get_winner(self):
        return self.winner

    def get_board(self):
        return self.board