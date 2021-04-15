#!/usr/bin/env python

import sys
from os import environ
from PyQt5.QtWidgets import QApplication

from view.main_view import MainView
from controller.main_controller import MainController

__version__ = '0.1'

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_view = MainView()
        self.main_controller = MainController(self.main_view)
        self.main_view.show()
    
def main():
    app = App(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    suppress_qt_warnings()
    main()
