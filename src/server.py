import sys
from resources.server import Server

if __name__ == '__main__':
    try:
        print("[STARTING] server is starting...")
        server = Server(sys.argv[1], int(sys.argv[2]))
        server.start()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)