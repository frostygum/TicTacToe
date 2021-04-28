
#! Import required python built-in modules
import json
from random import randint

class Board():
    """
        This class is used store in-game state
    """

    def __init__(self):
        """Function to create pre-defined state"""

        #! Initialize class scope variables
        self.size = 3
        self.symbols = ['X', 'O']
        self.turn = None
        self.move = 0
        self.gameState = {
            '00': None,
            '01': None,
            '02': None,
            '10': None,
            '11': None,
            '12': None,
            '20': None,
            '21': None,
            '22': None
        }
        self.player = {
            'host': None,
            'client': None
        }

        self.player['host'] = 'X' #? DEV
        #self.symbols[randint(0, 1)]
        self.player['client'] = self.findOponent(self.player['host'])
        #! Set turn to player that assigned as 'X' to play first
        self.turn = [player for player, symbol in self.player.items() if symbol == 'X'][0]

    def updateLocation(self, value, location):
        """Function to update symbol location in current state, location defined as xy"""
        
        #! Update the location with symbol
        self.gameState[location] = value

    def incrementMove(self):
        """Function to increment game move number"""

        #! Increment move, because
        self.move = self.move + 1

    def findOponent(self, player):
        """Function to update symbol location in current state"""

        #! Just check other symbol that doesn't used
        if player == self.symbols[0]:
            return self.symbols[1]
        else:
            return self.symbols[0]

    def switchTurn(self):
        """Function to switch current turn to opponent"""

        #! Set turn to opposite symbol
        if self.turn == 'host':
            self.turn = 'client'
        else:
            self.turn = 'host'

    def toJSON(self):
        """Function to dump current state as JSON string"""

        return json.dumps({
            'size': self.size,
            'turn': self.turn,
            'player': self.player,
            'move': self.move,
            'gamestate': self.gameState,
        })