
#! Import required python built-in modules
from functools import partial
#! Import required self-made modules
from model.board import Board
from controller.base_controller import BaseController

class GameController(BaseController):
    """
        This class is used as StartView Controller
    """
    
    def __init__(self, navigationWidget, views, serverThread, board, role):
        """Function to initiate game window settings"""

        #! Calling parent class init function
        BaseController.__init__(self, navigationWidget, views)
        
        self.board = board
        self.role = role
        self.serverThread = serverThread
        self.gameView.createTicTacToeGrid()
        self.connectSignals()

    def connectSignals(self):
        """Function to give the button ability"""

        for location, button in self.gameView.buttons.items():
            button.clicked.connect(partial(self.btnClicked, location))

    def btnClicked(self, location):
        """Button Ability when clicked"""

        playerSymbol = self.board.player['host']
        self.board.updateLocation(playerSymbol, location)
        self.gameView.updateButton(playerSymbol, location, False)
        self.board.incrementMove()
        print(self.board.toJSON())

        self.serverThread.sendState()

        if self.checkGameWinner() == False:
            self.board.switchTurn()
            self.checkRightTurn()

    def checkRightTurn(self):
        """Function to disable all button if current turn is no apropiate"""

        if self.board.turn != 'host':
            self.toggleButtons(False)
        else:
            self.toggleButtons(True)

    def checkGameWinner(self):
        """Function to check if current state has a winner"""

        winner = self.checkGameRules()
        if winner == 0:
            self.showDialog('Gave Over, Player {} Wins!'.format(self.board.turn), 'Game Over', self.gameOver)
            return True
        elif winner == 2:
            self.showDialog('Gave Over, It\'s a Tie!', 'Game Over', self.gameOver)
            return True

        return False

    def checkGameRules(self):
        """Function to check winner rules condition, 0: win, 1: no winner, 2: tie"""

        state = self.board.gameState
        condition = 1

        #! Why >= 5 ? Not possible have winner if 5 move have not reached
        if self.board.move >= 5:
            if state['00'] == state['01'] == state['02'] != None:
                condition = 0
            elif state['10'] == state['11'] == state['12'] != None:
                condition = 0
            elif state['20'] == state['21'] == state['22'] != None:
                condition = 0
            elif state['00'] == state['10'] == state['20'] != None:
                condition = 0
            elif state['01'] == state['11'] == state['21'] != None:
                condition = 0
            elif state['02'] == state['12'] == state['22'] != None:
                condition = 0
            elif state['00'] == state['11'] == state['22'] != None:
                condition = 0
            elif state['02'] == state['11'] == state['20'] != None:
                condition = 0
        #! Why 9 ? 9 move means all boxes has already filled with symbols but no one wins
        if self.board.move == 9:
            condition = 2

        return condition

    def toggleButtons(self, enable):
        """Function to handle when received update from opponent"""

        #! Set enable or disable to all button with given settings
        for xPos in range(0, self.board.size):
            for yPos in  range(0, self.board.size):
                location = '{}{}'.format(xPos, yPos)
                self.gameView.buttons[location].setEnabled(enable)

    def gameOver(self):
        """Function to handle when received update from opponent"""

        self.board = Board()
        self.serverThread.stop()
        #! Reset all button symbols
        for xPos in range(0, 3):
            for yPos in  range(0, 3):
                location = '{}{}'.format(xPos, yPos)
                self.gameView.updateButton(' ', location)
        self.changeWindow('start')
        