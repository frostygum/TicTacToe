
#! Import required python built-in modules
import json
from functools import partial
#! Import required PyQt5 modules
from PyQt5.QtCore import QThread
#! Import required self-made modules
from model.board import Board
from resources.server import ServerReceive
from controller.base_controller import BaseController

class ServerThread(BaseController):
    """
        This class is responsible for creating thread to manage server
    """

    board = None
    serverThread = None
    serverWorker = None

    def __init__(self, navigationWidget, views, controller, board):
        """Function to create box to store widgets"""

        #! Calling parent class init function
        BaseController.__init__(self, navigationWidget, views)

        self.board = board
        self.controller = controller
        self.mainView = views['start']
        self.gameView = views['game']
        
    def start(self):
        """Function to start the thread"""

        #! Thread initiation
        self.serverThread = QThread()
        self.serverWorker = ServerReceive()
        self.serverWorker.moveToThread(self.serverThread)

        #! Emited when thread signal and worker signal started
        self.serverThread.started.connect(self.serverWorker.run)
        self.serverWorker.started.connect(partial(self.mainView.createStatusBar, 'Waiting for Connection'))
        #! Emited when worker signal connected, means connected to client
        self.serverWorker.connected.connect(self.sendState)
        self.serverWorker.connected.connect(partial(self.changeWindow, 'game'))
        # self.serverWorker.connected.connect(self.controller['game'].createGameBoard)
        self.serverWorker.connected.connect(partial(self.gameView.createStatusBar, 'Connected to {}:{}'.format(self.serverWorker.HOST, self.serverWorker.PORT)))
        #! Emited when worker signal received, means received data(game state)
        self.serverWorker.received.connect(self.handleReceivedData)
        
        #! Start the thread
        self.serverThread.start()

    def handleReceivedData(self, gameBoard):
        """Function to handle received board from opponent"""

        #! If received data can't be parsed by JSON parser
        #! Prevent app from crashed
        try:
            board = json.loads(gameBoard)
            self.controller['game'].handleReceiveUpdate(board)
        except:
            pass

    def sendState(self):
        """Function to handle sending current game state as JSON string"""

        state = self.board.toJSON()
        self.serverWorker.send(state)

    def stop(self):
        """Function to properly stop the server"""

         #! Stop socket properly then destroy the thread
        self.serverWorker.stop()
        self.serverThread.terminate()