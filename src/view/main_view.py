from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStatusBar

class MainView(QMainWindow):
    # def __init__(self, model, main_controller):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TicTacToe')
        self.setFixedWidth(330)
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
                self.buttons[key] = QPushButton('x')
                self.buttons[key].setFixedSize(100, 100)
                buttonsLayout.addWidget(self.buttons[key], xPos, yPos)
                
        self.generalLayout.addLayout(buttonsLayout)