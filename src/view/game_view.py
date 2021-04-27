
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QGridLayout, QPushButton, QVBoxLayout, QMainWindow, QWidget, QStatusBar
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class GameView(QMainWindow):
    """
        This class is responsible for managing the game window views in the application 
    """

    #! Initialize class scope variables
    # centalWidget = None
    # verticalLayout = None
    buttons = {}
    
    def __init__(self):
        """Function to create box to store widgets"""

        #! Calling parent class init function
        super(GameView, self).__init__()
        self.setStyleSheet("QMainWindow { background-color: pink; }"
                            "QPushButton { font-size: 35px; background-color: cyan; border: none; border-radius: 5px; }"
                            "QPushButton:hover { background-color: white; }")
        # Set the central widget and the general layout
        self.verticalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.verticalLayout)

    def createTicTacToeGrid(self):
        """Create Tic Tac Toe Grid based on size, so that the grid is equal to size x size"""
        
        #! Prepare Grid Layout to store TicTacToe buttons
        buttonsLayout = QGridLayout()

        #! Loop to create button and assign to layout
        #! 3 is defined for this TicTacToe game
        for xPos in range(0, 3):
            for yPos in  range(0, 3):
                #! Create key for button location identifier xy
                location = '{}{}'.format(xPos, yPos)

                self.buttons[location] = QPushButton(' ')
                self.buttons[location].setFixedSize(100, 100)
                self.buttons[location].setCursor(QCursor(Qt.PointingHandCursor))
                self.buttons[location].setLayoutDirection(Qt.RightToLeft)

                buttonsLayout.addWidget(self.buttons[location], xPos, yPos)
                
        self.verticalLayout.addLayout(buttonsLayout)

    def updateButton(self, player, location, enable = True):
        """Function to update buttons symbol(text) at given location(position)"""

        self.buttons[location].setText(player)
        self.buttons[location].setEnabled(enable)

    def createStatusBar(self, msg):
        """Function to create status bar at GameView"""

        status = QStatusBar()
        status.showMessage(msg)
        self.setStatusBar(status)