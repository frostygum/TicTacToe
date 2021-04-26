import json

class Board():
    def __init__(self):
        self.size = 3
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

    def updateLocation(self, value, location):
        self.gameState[location] = value

    def toJSON(self):
        return json.dumps(self.gameState)