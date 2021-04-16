import sys
from functools import partial
from PyQt5.QtCore import QTimer
from resources.client import Client
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Worker(QObject):
    msg_str = pyqtSignal(str)

    def addClient(self, client):
        self.client = client

    def run(self):
        while True:
            # Here has error when closing app because of client.recv() is blocking
            try:
                msg = self.client.recv()
                if msg:
                    self.msg_str.emit(msg)
                    print(msg)
            except:
                pass

class MainController:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        try:
            self.client = Client('127.0.0.1', 7000)
            self.view.createStatusBar("Connected to 127.0.0.1:7000")
            self.clientRecv()
        except Exception as e:
            print("Error", e)
            self.disconnect()
            sys.exit(1)

    def disconnect(self):
        self.client.disconnect()

    def clientRecv(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.addClient(self.client)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.msg_str.connect(self.changeBtnColor)
        self.thread.start()
            
    def connectSignals(self):
        for key, btn in self.view.buttons.items():
            btn.clicked.connect(partial(self.btnClick, key))

    def btnClick(self, msg):
        self.client.send(msg)

    def changeBtnColor(self, targetBtn):
        self.view.buttons[targetBtn].setStyleSheet("background-color : yellow; border-style: none;")
        self.view.buttons[targetBtn].setEnabled(False)
        # QTimer.singleShot(5000, lambda: self.view.buttons[targetBtn].setDisabled(False))