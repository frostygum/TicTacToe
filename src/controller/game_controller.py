from functools import partial
from controller.base_controller import BaseController
from resources.client import Client
from model.board import Board

class GameController(BaseController):
    def __init__(self, navigationWidget, views, board):
        BaseController.__init__(self, navigationWidget, views)
        self.board = board
        self.gameView.createTicTacToeGrid()
        self.connectSignals()

    def connectSignals(self):
        for location, button in self.gameView.buttons.items():
            button.clicked.connect(partial(self.btnClicked, location))

    def btnClicked(self, location):
        self.board.updateLocation('X', location)
        self.gameView.updateButton('X', location, False)
        print(self.board.toJSON())
        if self.checkGameWinner():
            self.showDialog('Gave Over, Player X Wins', 'Game Over', self.gameOver)

    def checkGameWinner(self):
        state = self.board.gameState
        if state['00'] == state['01'] == state['02'] != None:
            print('Game Over')
            return True
        elif state['10'] == state['11'] == state['12'] != None:
            print('Game Over')
            return True
        elif state['20'] == state['21'] == state['22'] != None:
            print('Game Over')
            return True
        elif state['00'] == state['10'] == state['20'] != None:
            print('Game Over')
            return True
        elif state['01'] == state['11'] == state['21'] != None:
            print('Game Over')
            return True
        elif state['02'] == state['12'] == state['22'] != None:
            print('Game Over')
            return True
        elif state['00'] == state['11'] == state['22'] != None:
            print('Game Over')
            return True
        elif state['02'] == state['11'] == state['20'] != None:
            print('Game Over')
            return True
        return False

    def gameOver(self):
        self.board = Board()
        for xPos in range(0, self.board.size):
            for yPos in  range(0, self.board.size):
                location = '{}{}'.format(xPos, yPos)
                self.gameView.updateButton(' ', location)
        self.changeWindow('start')
        