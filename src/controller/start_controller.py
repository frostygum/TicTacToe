
#! Import required python built-in modules
import sys
import re
from functools import partial

class StartController():
    """
        This class is used as StartView Controller
    """

    def __init__(self, app):
        """Function to initiate start window settings"""
        
        self.app = app
        self.app.startView.createStatusBar('')
        self.connectSignals()
            
    def connectSignals(self):
        """Function to give the button ability"""

        self.app.startView.buttons['create'].clicked.connect(self.startGame)
        self.app.startView.buttons['join'].clicked.connect(self.joinGame)

    def checkIpValidity(self):
        """Function to check given ip valid or not"""

        ipAddress = self.app.startView.inputIp
        ipAddress = ipAddress.text()

        if ipAddress != '':
            #! Regex to match x.x.x.x, where x is 3 length digits
            if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ipAddress):
                return True

        return False

    def startGame(self):
        """Ability for start button to start the game as host"""

        #! Run the game when ip valid
        if self.checkIpValidity():
            self.app.setTargetIp(self.app.startView.inputIp.text())
            self.app.setRole('host')
            self.app.clearBoard()
            self.app.initServerThread()
            self.app.serverThread.start()
            self.app.startView.buttons['create'].setEnabled(False)
            self.app.startView.buttons['join'].setEnabled(False)
        else:
            self.app.showDialog('Please fill Ip address first', 'Alert')

    def joinGame(self):
        """Ability for join button to join the game to given address"""

        #! Run the game when ip valid
        if self.checkIpValidity():
            self.app.setTargetIp(self.app.startView.inputIp.text())
            self.app.setRole('client')
            self.app.clearBoard()
            self.app.initClientThread()
            self.app.clientThread.start()
            self.app.startView.buttons['join'].setEnabled(False)
            self.app.startView.buttons['create'].setEnabled(False)
        else:
            self.app.showDialog('Please fill Ip address first', 'Alert')