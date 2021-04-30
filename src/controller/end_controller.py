
#! Import required python built-in modules
import sys
import re
from functools import partial

class EndController():
    """
        This class is used as EndView Controller
    """

    def __init__(self, app):
        """Function to initiate end window settings"""
        
        self.app = app
        self.app.endView.createStatusBar('')
        self.connectSignals()
            
    def connectSignals(self):
        """Function to give the button ability"""

        self.app.endView.buttons['play'].clicked.connect(self.playGame)
        self.app.endView.buttons['exit'].clicked.connect(self.exitGame)

    def playGame(self):
        """Ability for play button to play again"""

    def exitGame(self):
        """Ability for exit button to return to start window"""

        #! Stop client and server thread
        if self.app.role == 'host':
            self.app.serverThread.stop()
        else:
            self.app.clientThread.stop()