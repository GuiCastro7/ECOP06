
from PyQt5 import QtCore, QtWidgets
from jogo_da_velha import JogoDaVelha

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

        self.jogo = JogoDaVelha()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jogo da Velha"))
        self.label.setText(_translate("MainWindow", "Vencedor:"))

    def make_move(self, x, y):
        winner = self.jogo.make_move(x, y)
        self.buttons[(x, y)].setText('X' if self.jogo.player_turn == 'O' else 'O')
        if winner:
            self.label.setText(f"Vencedor: {'O' if self.jogo.player_turn == 'X' else 'X'}")

    def reset_game(self):
        self.jogo.reset_game()
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
