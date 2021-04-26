import sys
import re
from functools import partial
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from controller.base_controller import BaseController
from resources.client import Client

# class Worker(QObject):
#     msg_str = pyqtSignal(str)

#     def addClient(self, client):
#         self.client = client

#     def run(self):
#         while True:
#             # Here has error when closing app because of client.recv() is blocking
#             try:
#                 msg = self.client.recv()
#                 if msg:
#                     self.msg_str.emit(msg)
#                     print(msg)
#             except:
#                 pass

class MainController(BaseController):
    def __init__(self, navigationWidget, views):
        BaseController.__init__(self, navigationWidget, views)
        self.navigationWidget.setWindowTitle('TicTacToe')
        self.navigationWidget.setFixedSize(330, 200)
        self.connectSignals()
        # try:
        #     self.client = Client('127.0.0.1', 7000)
        #     self.mainView.createStatusBar("Connected to 127.0.0.1:7000")
        #     self.clientRecv()
        # except Exception as e:
        #     print("Error", e)
        #     self.disconnect()
        #     sys.exit(1)

    # def clientRecv(self):
    #     self.thread = QThread()
    #     self.worker = Worker()
    #     self.worker.addClient(self.client)
    #     self.worker.moveToThread(self.thread)
    #     self.thread.started.connect(self.worker.run)
    #     self.worker.msg_str.connect(self.changeBtnColor)
    #     self.thread.start()
            
    def connectSignals(self):
        startBtn = self.mainView.buttons['start']
        joinBtn = self.mainView.buttons['join']
        startBtn.clicked.connect(partial(self.changeBtnColor))
        joinBtn.clicked.connect(partial(self.changeBtnColor))

    def checkIpValidity(self):
        ipAddress = self.mainView.inputIp
        ipAddress = ipAddress.text()

        if ipAddress != '':
            if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ipAddress):
                return True

        return False

    def changeBtnColor(self):
        if self.checkIpValidity():
            self.changeWindow('game')
        else:
            self.showDialog('Silahkan Isi Ip address terlebih dahulu', 'Alert')