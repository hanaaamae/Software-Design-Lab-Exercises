"""
File: chatserver.py
Server for a chat room.  Handles one client at a 
time and participates in the conversation.
"""

from socket import *
from codecs import decode
from chatclienthandler import ChatClientHandler


HOST = "localhost" 
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from: ", address)
    handler = ChatClientHandler(client, address)
    handler.start()
