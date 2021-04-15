#!/usr/bin/env python3

import sys
from os import environ
from functools import partial

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'

class View(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
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

# Create a Controller class to connect the GUI and the model
class Controller:
    """PyCalc Controller class."""
    def __init__(self, view):
        """Controller initializer."""
        self._view = view
        self._connectSignals()
    
    def _connectSignals(self):
        for x in self._view.buttons:
            print(x)

    def greeting(self):
        print("hello")

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = View()
    view.show() 
    # Create instances of the model and the controller
    Controller(view = view)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == '__main__':
    suppress_qt_warnings()
    main()
