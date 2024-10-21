from PyQt5 import QtCore, QtWidgets

class TicTacToeGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.player_turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(180, 110, 581, 371)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.buttons = {}
        
        for i in range(3):
            for j in range(3):
                button = QtWidgets.QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda checked, x=i, y=j: self.make_move(x, y))
                self.buttons[(i, j)] = button
                self.gridLayout.addWidget(button, i, j)

        self.label = QtWidgets.QLabel("Vencedor:")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)

        # Reset button
        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_game)
        self.gridLayout.addWidget(self.reset_button, 4, 0, 1, 3)

    def make_move(self, x, y):
        if self.board[x][y] == '' and not self.check_winner():
            self.board[x][y] = self.player_turn
            self.buttons[(x, y)].setText(self.player_turn)
            if self.check_winner():
                self.label.setText(f"Vencedor: {self.player_turn}")
            self.player_turn = 'O' if self.player_turn == 'X' else 'X'

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
        self.label.setText("Vencedor:")
        for button in self.buttons.values():
            button.setText("")
