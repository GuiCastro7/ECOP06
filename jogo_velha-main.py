
import sys
from PyQt5 import QtWidgets
from jogo_da_velha import TicTacToeGame

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game_window = TicTacToeGame()
    game_window.setWindowTitle("Jogo da Velha")
    game_window.show()
    sys.exit(app.exec_())
