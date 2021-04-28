
#! Import required python built-in modules
import json
from functools import partial
#! Import required PyQt5 modules
from PyQt5.QtCore import QThread
#! Import required self-made modules
from model.board import Board
from resources.client import ClientReceive

class ClientThread():
    """
        This class is responsible for creating thread to manage server
    """

    def __init__(self, app):
        """Function to create box to store widgets"""

        self.app = app
        
    def start(self):
        """Function to start the thread"""
        
        #! Set current player role
        self.app.gameController.role = 'host'

        #! Thread initiation
        self.clientReceiveThread = QThread()
        self.clientReceiveWorker = ClientReceive()
        self.clientReceiveWorker.moveToThread(self.clientReceiveThread)

        #! Emited when thread signal and worker signal started
        self.clientReceiveThread.started.connect(partial(self.clientReceiveWorker.run, host=self.app.targetIp))
        # self.clientReceiveWorker.started.connect(partial(self.app.startView.createStatusBar, 'Waiting for Connection'))
        #! Emited when worker signal connected, means connected to client
        self.clientReceiveWorker.connected.connect(self.handleConnected)
        #! Emited when worker signal received, means received data(game state)
        self.clientReceiveWorker.received.connect(self.handleReceivedData)
        #! Emited when worker signal error, means server can'y bind to given address
        self.clientReceiveWorker.error.connect(self.handleError)
        #! Emited when worker signal disconnected, means client has been disconected
        self.clientReceiveWorker.disconnected.connect(self.handleDisconnected)
        
        #! Start the thread
        self.clientReceiveThread.start()

    def handleReceivedData(self, gameBoard):
        """Function to handle received board from opponent"""

        #! If received data can't be parsed by JSON parser
        #! Prevent app from crashed
        try:
            board = json.loads(gameBoard)
            self.app.gameController.handleReceiveUpdate(board)
        except Exception as e:
            print('ERROR[HRD-CT]', e)

    def handleDisconnected(self):
        try:
            self.clientReceiveThread.terminate()
            self.serverReceiveWorker = None
            self.app.changeWindow('start')
        except Exception as e:
            print('ERROR[HD-CT]', e)

    def sendState(self):
        """Function to handle sending current game state as JSON string"""

        state = self.app.board.toJSON()
        self.clientReceiveWorker.send(state)

    def handleConnected(self, addressInfo):
        """Function to handle new connection emited"""

        addressInfo = json.loads(addressInfo)

        self.app.gameView.title.setText('You are [{}]'.format(self.app.board.player[self.app.role]))
        self.app.changeWindow('game')
        self.app.gameView.createStatusBar('Connected to {}:{}'.format(addressInfo['host'], addressInfo['port']))

    def handleError(self):
        """Function to handle error when creating socket emited"""

        self.app.showDialog(msg='Failed to connect to given address', title='Error')
        self.clientReceiveThread.terminate()
        self.clientReceiveWorker = None

    def stop(self):
        """Function to properly stop the server"""

         #! Stop socket properly then destroy the thread
        self.clientReceiveWorker.stop()
        self.clientReceiveThread.terminate()
        self.clientReceiveWorker = None