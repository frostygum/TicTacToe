
#! Import required python built-in modules
import sys
from os import environ
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMessageBox
#! Import required self-made modules
from view.start_view import StartView
from view.game_view import GameView
from model.board import Board
from controller.start_controller import StartController
from controller.game_controller import GameController
from controller.serverThread import ServerThread
from controller.clientThread import ClientThread

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class App(QApplication):
    def __init__(self, sys_argv):
        """Function to instantiate app"""

        super(App, self).__init__(sys_argv)

        self.navigationWidget = QStackedWidget()
        self.board = Board()
        self.role = None
        self.targetIp = None

        self.startView = StartView()
        self.gameView = GameView()
        
        self.startController = StartController(self)
        self.gameController = GameController(self)
        # self.initServerThread()
        
        self.navigationWidget.setWindowTitle('TicTacToe')
        self.navigationWidget.setFixedSize(330, 200)
        self.navigationWidget.addWidget(self.startView)
        self.navigationWidget.show()

    def initServerThread(self):
        """Function to instantiate server"""

        self.serverThread = None
        self.serverThread = ServerThread(self)

    def initClientThread(self):
        """Function to instantiate client connection"""

        self.clientThread = None
        self.clientThread = ClientThread(self)
    
    def changeWindow(self, windowPage):
        """Function to change window with given param"""

        if(windowPage == 'start'):
            #! Goto Main Page
            window = self.startView
            controller = self.startController
            #! Reset sizing
            self.navigationWidget.setFixedSize(330, 200)
        elif(windowPage == 'game'):
            #! Goto GGame Page
            window = self.gameView
            controller = self.gameController
            #! Reset sizing
            self.navigationWidget.setFixedSize(330, 400)
        
        #! Create empty status bar
        window.createStatusBar('')
        # window = window()
        # controller = controller(self)
        self.navigationWidget.addWidget(window)
        self.navigationWidget.setCurrentIndex(self.navigationWidget.currentIndex() + 1)

    def clearBoard(self):
        """Function to clear current board"""

        self.board = None
        self.board = Board()

        for xPos in range(0, 3):
            for yPos in  range(0, 3):
                location = '{}{}'.format(xPos, yPos)
                self.gameView.updateButton(' ', location)

    def setRole(self, role):
        """Function to change app role"""

        self.role = role

    def setTargetIp(self, ipAddress):
        """Function to change app target ip address"""

        self.targetIp = ipAddress

    def showDialog(self, msg, title, callback = None):
        """Function to show Alert Dialog"""

        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.exec()
        #! Run any given callback after user close the dialog
        if callback != None:
            callback()

def main():
    app = App(sys.argv)
    exec = app.exec_()
    # app.main_controller.disconnect()
    sys.exit(exec)

if __name__ == '__main__':
    suppress_qt_warnings()
    main()
