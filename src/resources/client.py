
#! Import required python built-in modules
import socket
import sys
import json
#! Import required PyQt5 modules
from PyQt5.QtCore import QObject, pyqtSignal

class ClientReceive(QObject):
    """
        This class is used to connect to given ip address and port (server), it is also responsible 
        for waiting for json data from the server. This class is used as a worker class from the 
        QThread class in PyQt5.
    """

    #! Preserved thread signals
    started = pyqtSignal(bool)
    connected = pyqtSignal(str)
    received = pyqtSignal(str)
    disconnected = pyqtSignal(bool)
    error = pyqtSignal(bool)
    #! Initialize class scope variables
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = 7000
    HOST = DEFAULT_HOST
    PORT = DEFAULT_PORT
    HEADER = 1024
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = '!DISCONNECT'

    def createSocket(self):
        """Function to create and connect socket at given address"""

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.HOST, self.PORT))
            return True
        except Exception as e:
            print('ERROR[CR-C]', e)
            return False

    def handleReceive(self):
        """Function to handle receiving json game data"""

        print('[NEW CONNECTION] {} connected.'.format((self.HOST, self.PORT)))
        #! Emit connected signal
        self.connected.emit(json.dumps({
            'host': self.HOST,
            'port': self.PORT
        }))
        #! Initialize variables
        connected = True
        data = None
        
        #! Loop when host connected to client
        while connected:
            try:
                #! Receiving data.
                data = self.client.recv(self.HEADER).decode(self.FORMAT)
                if data == self.DISCONNECT_MESSAGE:
                    connected = False
                else:
                    #! Send received signal and the received data
                    self.received.emit(data)
            except:
                #! If there is any troble with connection, assumed that client is disconnected
                print('[{}] Disconnected.'.format((self.HOST, self.PORT)))
                connected = False
                #! Close connection with client
                self.client.close()
        #! Send disconnected signal
        self.disconnected.emit(True)

    def send(self, msg):
        self.client.send(msg.encode(self.FORMAT))

    def run(self, host = None, port = None):

        #! Bind given param to class scope variable
        if host != None: self.HOST = host
        if port != None: self.PORT = port
        
        if self.createSocket():
            self.handleReceive()
            #! Send started signal
            self.started.emit(True)
        else:
            self.error.emit(True)

    def stop(self):
        """Function to properly close socket connection"""

        # self.send(self.DISCONNECT_MESSAGE)
        self.client.close()