
#! Import required python built-in modules
import json
from functools import partial
#! Import required PyQt5 modules
from PyQt5.QtCore import QThread
#! Import required self-made modules
from model.board import Board
from resources.server import ServerReceive

class ServerThread():
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
        self.serverReceiveThread = QThread()
        self.serverReceiveWorker = ServerReceive()
        self.serverReceiveWorker.moveToThread(self.serverReceiveThread)

        #! Emited when thread signal and worker signal started
        self.serverReceiveThread.started.connect(self.serverReceiveWorker.run)
        self.serverReceiveWorker.started.connect(partial(self.app.startView.createStatusBar, 'Waiting for Connection'))
        #! Emited when worker signal connected, means connected to client
        self.serverReceiveWorker.connected.connect(self.sendState)
        self.serverReceiveWorker.connected.connect(partial(self.app.changeWindow, 'game'))
        # self.serverReceiveWorker.connected.connect(self.app.gameController.createGameBoard)
        self.serverReceiveWorker.connected.connect(partial(self.app.gameView.createStatusBar, 'Connected to {}:{}'.format(self.serverReceiveWorker.HOST, self.serverReceiveWorker.PORT)))
        #! Emited when worker signal received, means received data(game state)
        self.serverReceiveWorker.received.connect(self.handleReceivedData)
        
        #! Start the thread
        self.serverReceiveThread.start()

    def handleReceivedData(self, gameBoard):
        """Function to handle received board from opponent"""

        #! If received data can't be parsed by JSON parser
        #! Prevent app from crashed
        try:
            board = json.loads(gameBoard)
            self.app.gameController.handleReceiveUpdate(board)
        except Exception as e:
            print(e)

    def sendState(self):
        """Function to handle sending current game state as JSON string"""

        state = self.app.board.toJSON()
        self.serverReceiveWorker.send(state)

    def stop(self):
        """Function to properly stop the server"""

         #! Stop socket properly then destroy the thread
        self.serverReceiveWorker.stop()
        self.serverReceiveThread.terminate()
        self.serverReceiveWorker = None