import socket 
import threading
import sys

class Server():
    def __init__(self, HOST = '127.0.0.1', PORT = 7000):
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (self.HOST, self.PORT)
        self.HEADER = 1024
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.client = []
        self.create_socket()

    def create_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True

        while connected:
            data = conn.recv(self.HEADER)
            if data:
                data = int(data)
                msg = conn.recv(data).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] {msg}")
                conn.send(msg.encode(self.FORMAT))

        conn.close()
        self.client.pop()

    def create_client(self, conn, addr):
        self.client.append(addr)
        thread = threading.Thread(target = self.handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.HOST}")
    
        while True:
            conn, addr = self.server.accept()
            if (threading.activeCount() - 1) < 2:
                self.create_client(conn, addr)
            else:
                conn.close()