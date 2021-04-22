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
        self.DISCONNECT_MESSAGE = '!DISCONNECT'
        self.client = None
        self.create_socket()

    def create_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def handle_reply(self):
        conn, addr = self.client
        print('[NEW CONNECTION] {} connected.'.format(addr))
        connected = True

        while connected:
            try:
                msg = conn.recv(self.HEADER).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
            except:
                print('[{}] Disconnected.'.format(addr))
                self.wait_client()
                connected = False
                break

            print('[{}] {}'.format(addr, msg))

        conn.close()
    
    def wait_client(self):
        conn, addr = self.server.accept()
        self.create_client(conn, addr)

    def send(self, msg):
        conn, addr = self.client
        message = msg.encode(self.FORMAT)
        conn.send(message)

    def create_client(self, conn, addr):
        self.client = (conn, addr)
        reply_thread = threading.Thread(target = self.handle_reply)
        
        reply_thread.start()
        print('[ACTIVE CONNECTIONS] {}'.format(threading.activeCount() - 1))
        
    def start(self):
        self.server.listen()
        print('[LISTENING] Server is listening on {}'.format(self.HOST))
    
        self.wait_client()

        # while True:
        #     reply = input()
        #     conn, _ = self.client
        #     conn.send(reply.encode(self.FORMAT))

# if __name__ == '__main__':
#     server = Server()
#     try:
#         server.start()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         sys.exit(0)