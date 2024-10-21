# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jogo_da_velha.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 110, 581, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.buttons = {}
        for i in range(3):
            for j in range(3):
                button = QtWidgets.QPushButton("")
                button.setObjectName(f"pushButton_{i * 3 + j + 1}")
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda checked, x=i, y=j: self.make_move(x, y))
                self.buttons[(i, j)] = button
                self.gridLayout.addWidget(button, i, j)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 53, 541, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        # Reset button
        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.setGeometry(QtCore.QRect(450, 490, 100, 30))
        self.reset_button.clicked.connect(self.reset_game)
        self.reset_button.setParent(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.player_turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jogo da Velha"))
        self.label.setText(_translate("MainWindow", "Vencedor:"))

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())