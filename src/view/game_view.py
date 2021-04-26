from PyQt5.QtWidgets import QGridLayout, QPushButton, QVBoxLayout, QMainWindow, QWidget, QStatusBar
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class GameView(QMainWindow):
    def __init__(self):
        super(GameView, self).__init__()
        self.setStyleSheet("QMainWindow { background-color: pink; }"
                            "QPushButton { font-size: 35px; background-color: cyan; border: none; border-radius: 5px; }"
                            "QPushButton:hover { background-color: white; }")
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        # Create the display and the buttons
        self.buttons = {}
    
    def createStatusBar(self, msg):
        status = QStatusBar()
        status.showMessage(msg)
        self.setStatusBar(status)

    def createTicTacToeGrid(self, board):
        """Create Tic Tac Toe Grid based on size, so that the grid is equal to size x size"""
        buttonsLayout = QGridLayout()

        for xPos in range(0, board.size):
            for yPos in  range(0, board.size):
                location = '{}{}'.format(xPos, yPos)

                self.buttons[location] = QPushButton(' ')
                self.buttons[location].setFixedSize(100, 100)
                self.buttons[location].setCursor(QCursor(Qt.PointingHandCursor))
                self.buttons[location].setLayoutDirection(Qt.RightToLeft)

                buttonsLayout.addWidget(self.buttons[location], xPos, yPos)
                
        self.generalLayout.addLayout(buttonsLayout)

    def updateButton(self, player, location, enable=True):
        self.buttons[location].setText(player)
        self.buttons[location].setEnabled(enable)