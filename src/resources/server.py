
#! Import required python built-in modules
import socket 
import sys
import json
from functools import partial
#! Import required PyQt5 modules
from PyQt5.QtCore import QObject, pyqtSignal

class ServerReceive(QObject):
    """
        This class is used to create a server at a given ip address and port, it is also responsible 
        for waiting for data in the form of json from the client. This class is used as a working class 
        from the QThread class in PyQt5.
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
        """Function to create socket at given address"""

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.HOST, self.PORT))
            self.server.listen(1)
            #! Send started signal
            self.started.emit(True)
            return True
        except Exception as e:
            print('ERROR', e)
            self.error.emit(True)
            return False

    def handleReceive(self):
        """Function to handle receiving json game data"""

        connection, addressInfo = self.client
        print('[NEW CONNECTION] {} connected.'.format(addressInfo))
        #! Initialize variables
        connected = True
        data = None

        #! Loop when host connected to client
        while connected:
            try:
                #! Receiving data.
                data = connection.recv(self.HEADER).decode(self.FORMAT)
                if data == self.DISCONNECT_MESSAGE:
                    connected = False
                else:
                    #! Send received signal and the received data
                    self.received.emit(data)
            except:
                #! If there is any troble with connection, assumed that client is disconnected
                print('[{}] Disconnected.'.format(addressInfo))
                connected = False
                #! Close connection with client
                connection.close()
                self.server.close()
        #! Send disconnected signal
        self.disconnected.emit(True)
    
    def waitClient(self):
        """Function to wait incoming connection from client"""

        connection, addressInfo = self.server.accept()
        self.client = (connection, addressInfo)
        #! Send connected signal
        self.connected.emit(json.dumps({
            'host': addressInfo[0],
            'port': addressInfo[1]
        }))
        #! Start receiving loop
        self.handleReceive()

    def send(self, msg):
        """Function to send string message to client"""

        connection, _ = self.client
        connection.send(msg.encode(self.FORMAT))

    def run(self, host = None, port = None):
        """Function to create server and should be called first when using thread"""

        #! Bind given param to class scope variable
        if host != None: self.HOST = host
        if port != None: self.PORT = port
        
        if self.createSocket():
            print('[LISTENING] Server is listening on {}'.format(self.HOST))
            self.waitClient()

    def closeServer(self):
        """Function to properly close server port binding"""
        self.server.close()

    def stop(self):
        """Function to properly close socket connection"""

        connection, _ = self.client
        #! Send disconnect message
        self.send(self.DISCONNECT_MESSAGE)
        #! Close connection
        connection.close()
        self.closeServer()