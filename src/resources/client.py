import socket
import threading
import sys

class Client():
    def __init__(self, HOST = '127.0.0.1', PORT = 7000):
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (self.HOST, self.PORT)
        self.HEADER = 1024
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!DISCONNECT'
        self.create_socket()

    def create_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR) 

    def handle_reply(self):
        print('[NEW CONNECTION] {} connected.'.format(self.ADDR))
        connected = True
        
        while connected:
            try:
                msg = self.client.recv(self.HEADER).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
            except:
                print('Error')
                connected = False
                break

            print('[{}] {}'.format(self.ADDR, msg))
        self.client.close()

    def create_host(self):
        thread = threading.Thread(target = self.handle_reply)
        thread.start()

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        self.client.send(message)

    def disconnect(self):
        self.send(self.DISCONNECT_MESSAGE)

    def start(self):
        self.create_host()
        try:
            while True:
                reply = input()
                self.send(reply)
        except:
            print('error')

if __name__ == '__main__':
    client = Client()
    try: 
        client.start()
    except KeyboardInterrupt:
        print('Interrupted')
        client.disconnect()
        sys.exit(0)