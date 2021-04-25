#!/usr/bin/env python

import sys
from os import environ
from PyQt5.QtWidgets import QApplication, QStackedWidget

from view.main_view import MainView
from view.game_view import GameView 
from controller.main_controller import MainController
from controller.game_controller import GameController
from model.board import Board

__version__ = '0.1'

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        views = {}
        views['main'] = MainView()
        views['game'] = GameView()
        self.navigationWidget = QStackedWidget()

        board = Board()
        self.main_controller = MainController(self.navigationWidget, views)
        self.game_controller = GameController(self.navigationWidget, views, board)

        self.navigationWidget.setWindowTitle('TicTacToe')
        self.navigationWidget.setFixedSize(330, 200)
        self.navigationWidget.addWidget(views['main'])
        self.navigationWidget.show()

def main():
    app = App(sys.argv)
    exec = app.exec_()
    # app.main_controller.disconnect()
    sys.exit(exec)

if __name__ == '__main__':
    suppress_qt_warnings()
    main()
