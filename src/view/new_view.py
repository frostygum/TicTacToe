import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor

class HomeView(QMainWindow):
    def __init__(self):
        super(HomeView, self).__init__()
        loadUi("src/view/home.ui", self)
        self.setStyleSheet("QMainWindow { background-color: pink; }"
                                "QPushButton { background-color: cyan; }")
        self.button_start.clicked.connect(self.print)
        self.button_join.clicked.connect(self.createGameView)

    def print(self):
        if(self.edit_ip.text() == ''):
            msgBox = QMessageBox()
            msgBox.setText("Mohon masukkan IP terlebih dahulu.")
            msgBox.exec()
        else:
            print(self.edit_ip.text())

    def createGameView(self):
        gameView = GameView()
        widget.addWidget(gameView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class GameView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QMainWindow { background-color: pink; }"
                                "QPushButton { font-size: 70px; background-color: cyan; border: none; }"
                                "QPushButton:hover { background-color: white; }")
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self.size = 3
        self.createTicTacToeGrid()
    
    def createStatusBar(self, msg):
        status = QStatusBar()
        status.showMessage(msg)
        self.setStatusBar(status)

    def createTicTacToeGrid(self):
        """Create Tic Tac Toe Grid based on size, so that the grid is equal to size x size"""
        self.buttons = {}
        buttonsLayout = QGridLayout()

        for xPos in range(0, self.size):
            for yPos in  range(0, self.size):
                key = '{}{}'.format(xPos, yPos)
                self.buttons[key] = QPushButton()
                self.buttons[key].setFixedSize(100, 100)
                self.buttons[key].setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                buttonsLayout.addWidget(self.buttons[key], xPos, yPos)
                
        self.generalLayout.addLayout(buttonsLayout)

app = QApplication(sys.argv)
homeView = HomeView()
widget = QtWidgets.QStackedWidget()

widget.addWidget(homeView)
widget.setWindowTitle('TicTacToe')
widget.setFixedSize(330, 330)
widget.show()
sys.exit(app.exec_())