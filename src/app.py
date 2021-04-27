
#! Import required python built-in modules
import sys
from os import environ
#! Import required PyQt5 modules
from PyQt5.QtWidgets import QApplication, QStackedWidget
#! Import required self-made modules
from model.board import Board
from view.start_view import StartView
from view.game_view import GameView
from controller.start_controller import StartController
from controller.game_controller import GameController
from controller.serverThread import ServerThread

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class App(QApplication):
    def __init__(self, sys_argv):

        super(App, self).__init__(sys_argv)

        navigationWidget = QStackedWidget()
        board = Board()
        views = {}
        controller = {}

        views['start'] = StartView()
        views['game'] = GameView()
        serverThread = ServerThread(navigationWidget, views, controller)
        controller['start'] = StartController(navigationWidget, views, serverThread)
        controller['game'] = GameController(navigationWidget, views, board, serverThread)
        
        navigationWidget.setWindowTitle('TicTacToe')
        navigationWidget.setFixedSize(330, 200)
        navigationWidget.addWidget(views['start'])
        navigationWidget.show()

def main():
    app = App(sys.argv)
    exec = app.exec_()
    # app.main_controller.disconnect()
    sys.exit(exec)

if __name__ == '__main__':
    suppress_qt_warnings()
    main()
