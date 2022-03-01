# This is a comment

import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
