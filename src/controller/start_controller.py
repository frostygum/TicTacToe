
#! Import required python built-in modules
import sys
import re
from functools import partial
#! Import required self-made modules
from controller.base_controller import BaseController

class StartController(BaseController):
    """
        This class is used as StartView Controller
    """

    navigationWidget = None
    mainView = None

    def __init__(self, navigationWidget, views):
        """Function to initiate start window settings"""
        
        #! Calling parent class init function
        BaseController.__init__(self, navigationWidget, views)
        
        self.navigationWidget.setWindowTitle('TicTacToe')
        self.navigationWidget.setFixedSize(330, 200)
        self.mainView.createStatusBar('')
        self.connectSignals()
            
    def connectSignals(self):
        """Function to give the button ability"""

        self.mainView.buttons['create'].clicked.connect(partial(self.startGame))
        self.mainView.buttons['join'].clicked.connect(partial(print, 'ok'))

    def checkIpValidity(self):
        """Function to check given ip valid or not"""

        ipAddress = self.mainView.inputIp
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
            self.changeWindow('game')
        else:
            self.showDialog('Silahkan Isi Ip address terlebih dahulu', 'Alert')