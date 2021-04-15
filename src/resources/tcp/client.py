import socket
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def run():
    while True:
        msg = input()
        if(msg != "exit"):
            send(msg)
        else:
            send(DISCONNECT_MESSAGE)
            break


if __name__ == '__main__':
    try:
        print("[STARTING] server is starting...")
        run()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)