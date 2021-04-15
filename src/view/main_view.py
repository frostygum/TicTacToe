from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

class MainView(QMainWindow):
    # def __init__(self, model, main_controller):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TicTacToe')
        self.setFixedSize(330, 330)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self.size = 3
        self._createTicTacToeGrid()

    def _createTicTacToeGrid(self):
        """Create Tic Tac Toe Grid based on size, so that the grid is equal to size x size"""
        self.buttons = [[0] * self.size] * self.size
        buttonsLayout = QGridLayout()

        for xPos in range(0, self.size):
            for yPos in  range(0, self.size):
                self.buttons[xPos][yPos] = QPushButton('x')
                self.buttons[xPos][yPos].setFixedSize(100, 100)
                buttonsLayout.addWidget(self.buttons[xPos][yPos], xPos, yPos)

        self.generalLayout.addLayout(buttonsLayout)