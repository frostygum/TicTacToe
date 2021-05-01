
#! Import required python built-in modules
import json
from functools import partial
#! Import required PyQt5 modules
from PyQt5.QtCore import QThread
#! Import required self-made modules
from src.model.board import Board
from src.resources.server import ServerReceive

class ServerThread():
    """
        This class is responsible for creating thread to manage server
    """

    def __init__(self, app):
        """Function to create box to store widgets"""

        self.app = app
        self.disconnected = False
        self.again = False
        
    def start(self):
        """Function to start the thread"""
        
        #! Set current player role
        self.app.gameController.role = 'host'

        #! Thread initiation
        self.serverReceiveThread = QThread()
        self.serverReceiveWorker = ServerReceive()
        self.serverReceiveWorker.moveToThread(self.serverReceiveThread)

        #! Emited when thread signal and worker signal started
        self.serverReceiveThread.started.connect(partial(self.serverReceiveWorker.run, host=self.app.targetIp))
        self.serverReceiveWorker.started.connect(partial(self.app.startView.createStatusBar, 'Waiting for Connection'))
        #! Emited when worker signal connected, means connected to client
        self.serverReceiveWorker.connected.connect(self.handleConnected)
        #! Emited when worker signal received, means received data(game state)
        self.serverReceiveWorker.received.connect(self.handleReceivedData)
        #! Emited when worker signal error, means server can'y bind to given address
        self.serverReceiveWorker.error.connect(self.handleError)
        #! Emited when worker signal disconnected, means client has been disconected
        self.serverReceiveWorker.disconnected.connect(self.handleDisconnected)
        #! Emited when worker signal get request to play again
        self.serverReceiveWorker.playAgain.connect(self.handlePlayAgain)
        
        #! Start the thread
        self.serverReceiveThread.start()

    def handleReceivedData(self, message):
        """Function to handle received message from opponent"""

        #! If received data can't be parsed by JSON parser (not a board)
        #! Check if received data = 'again'
        #! Prevent app from crashed
        try:
            board = json.loads(message)
            self.app.gameController.handleReceiveUpdate(board)
        except Exception as e:
            print('ERROR[HRD-ST]', e)

    def handleDisconnected(self):
        try:
            self.disconnected = True
            self.serverReceiveThread.terminate()
            self.serverReceiveWorker = None
            self.app.round = 1
            self.app.hostCount = 0
            self.app.clientCount = 0
            self.app.endView.emptyList()
            self.app.changeWindow('start')
        except Exception as e:
            print('ERROR[HD-ST]', e)

    def sendState(self):
        """Function to handle sending current game state as JSON string"""

        state = self.app.board.toJSON()
        self.serverReceiveWorker.send(state)

    def handleConnected(self, addressInfo):
        """Function to handle new connection emited"""

        addressInfo = json.loads(addressInfo)

        self.sendState()
        self.app.gameView.title.setText('Hello {}, You are [{}]'.format(self.app.role.upper(), self.app.board.player[self.app.role]))
        self.app.changeWindow('game')
        self.app.startView.buttons['join'].setEnabled(True)
        self.app.startView.buttons['create'].setEnabled(True)
        self.app.gameController.checkRightTurn()
        self.app.gameView.createStatusBar('Connected to {}:{}'.format(addressInfo['host'], addressInfo['port']))

    def handleError(self):
        """Function to handle error when creating socket emited"""

        self.app.showDialog(msg='Failed to connect to given address', title='Error')
        self.app.startView.buttons['create'].setEnabled(True)
        self.app.startView.buttons['join'].setEnabled(True)
        self.serverReceiveThread.terminate()
        self.serverReceiveWorker = None

    def stop(self):
        """Function to properly stop the server"""

        if self.disconnected == False:
            #! Stop socket properly then destroy the thread
            self.serverReceiveWorker.stop()
            self.serverReceiveThread.terminate()
            self.serverReceiveWorker = None

    def sendAgain(self):
        """Function to handle message for play again"""

        self.serverReceiveWorker.requestPlayAgain()
        self.app.endView.createStatusBar('Waiting for Other Player to Join')
        self.handlePlayAgain()

    def handlePlayAgain(self):
        """Function to handle play again condition"""

        if self.again == True:
            self.sendState()
            self.app.gameView.title.setText('Hello {}, You are [{}]'.format(self.app.role.upper(), self.app.board.player[self.app.role]))
            self.app.changeWindow('game')
            self.app.endView.buttons['play'].setEnabled(True)
            self.app.endView.buttons['exit'].setEnabled(True)
            self.app.gameController.checkRightTurn()
            self.again = False
        else:
            self.again = True