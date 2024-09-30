from PyQt5 import QtWidgets

class JogoDaVelha:
    def __init__(self):
        self.player_turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def make_move(self, x, y):
        if self.board[x][y] == '' and not self.check_winner():
            self.board[x][y] = self.player_turn
            self.player_turn = 'O' if self.player_turn == 'X' else 'X'
            return self.check_winner()
        return False

    def check_winner(self):
        for line in self.board:
            if line[0] == line[1] == line[2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def reset_game(self):
        self.player_turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
