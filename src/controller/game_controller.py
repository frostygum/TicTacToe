
#! Import required python built-in modules
from functools import partial
#! Import required self-made modules
from src.model.board import Board

class GameController():
    """
        This class is used as StartView Controller
    """
    
    def __init__(self, app):
        """Function to initiate game window settings"""
        
        self.app = app
        self.app.gameView.createTicTacToeGrid()
        self.connectSignals()

    def connectSignals(self):
        """Function to give the button ability"""

        for location, button in self.app.gameView.buttons.items():
            button.clicked.connect(partial(self.handleBtnClicked, location))

    def handleBtnClicked(self, location):
        """Button Ability when clicked"""

        playerSymbol = self.app.board.player[self.app.role]
        self.app.board.updateLocation(playerSymbol, location)
        self.app.gameView.updateButton(playerSymbol, location, False)
        self.app.board.incrementMove()
        self.app.board.switchTurn()
        
        if self.app.role == 'host':
            self.app.serverThread.sendState()
        else:
            self.app.clientThread.sendState()

        if self.checkGameWinner() == False:
            self.checkRightTurn()

        print(self.app.board.toJSON())

    def handleReceiveUpdate(self, gameBoard):
        """Function to handle when received update from opponent"""

        opponentSymbol = self.app.board.findOponent(self.app.board.player[self.app.role])

        for location, symbol in gameBoard['gamestate'].items():
            if symbol == opponentSymbol:
                self.app.board.updateLocation(symbol, location)
                self.app.gameView.updateButton(symbol, location, False)

        if self.app.board.player != gameBoard['player']:
            self.app.board.player = gameBoard['player']
            self.app.gameView.title.setText('You are [{}]'.format(self.app.board.player[self.app.role]))
        
        self.app.board.turn = gameBoard['turn']
        self.app.board.move = gameBoard['move']

        print(self.app.board.toJSON())
        
        if self.checkGameWinner() == False:
            self.checkRightTurn()

    def checkRightTurn(self):
        """Function to disable all button if current turn is no apropiate"""

        #! Set enable or disable to all button with given settings
        for xPos in range(0, 3):
            for yPos in  range(0, 3):
                location = '{}{}'.format(xPos, yPos)
                #! Disable button when current is not my turn
                if self.app.board.turn != self.app.role:
                    self.app.gameView.subTitle.setText('waiting for opponent')
                    self.app.gameView.buttons[location].setEnabled(False)
                else:
                    #! Enable only empty button when current is my turn, disable the other
                    self.app.gameView.subTitle.setText('It\'s your turn')
                    if self.app.board.gameState[location] == None:
                        self.app.gameView.buttons[location].setEnabled(True)
                    else:
                        self.app.gameView.buttons[location].setEnabled(False)

    def checkGameWinner(self):
        """Function to check if current state has a winner"""

        winner = self.checkGameRules()
        if winner == 0:
            self.app.showDialog('Gave Over, Player {} Wins!'.format(self.app.board.findOponent(self.app.board.player[self.app.board.turn])), 'Game Over', self.gameOver)
            return True
        elif winner == 2:
            self.app.showDialog('Gave Over, It\'s a Tie!', 'Game Over', self.gameOver)
            return True

        return False

    def checkGameRules(self):
        """Function to check winner rules condition, 0: win, 1: no winner, 2: tie"""

        state = self.app.board.gameState
        condition = 1

        #! Why >= 5 ? Not possible have winner if 5 move have not reached
        if self.app.board.move >= 5:
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
        if self.app.board.move == 9:
            condition = 2

        return condition

    def toggleButtons(self, enable):
        """Function to handle when received update from opponent"""

        #! Set enable or disable to all button with given settings
        for xPos in range(0, self.app.board.size):
            for yPos in  range(0, self.app.board.size):
                location = '{}{}'.format(xPos, yPos)
                self.app.gameView.buttons[location].setEnabled(enable)

    def gameOver(self):
        """Function to handle when received update from opponent"""

        # if self.app.role == 'host':
        #     self.app.serverThread.stop()
        # else:
        #     self.app.clientThread.stop()
        #! Reset all button symbols
        self.app.changeWindow('end')