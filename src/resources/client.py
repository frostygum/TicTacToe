import socket
import sys

class Client():
    def __init__(self, HOST = '127.0.0.1', PORT = 7000):
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (self.HOST, self.PORT)
        self.HEADER = 1024
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.create_socket()

    def create_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def recv(self):
        return self.client.recv(self.HEADER).decode(self.FORMAT)

    def disconnect(self):
        self.send(self.DISCONNECT_MESSAGE)

if __name__ == '__main__':
    try:
        client = Client()
        client.send(input())
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)