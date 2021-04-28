
#! Import required python built-in modules
import sys
from os import environ
#! Import required self-made modules
from src.app import App

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def main():
    app = App(sys.argv)
    exec = app.exec_()
    sys.exit(exec)

if __name__ == '__main__':
    suppress_qt_warnings()
    main()