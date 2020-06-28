"""
File: doctorserver.py
Server for providing non-directive psychotherapy.
Uses client handlers to handle clients' requests.
"""

from socket import *
from doctorclienthandler import DoctorClientHandler

HOST = "localhost"
PORT = 4321
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now just waits for connections from clients
# and hands sockets off to client handlers
try:
	while True:
	    print("Waiting for connection . . .")
	    client, address = server.accept()
	    print(str(client), str(address))
	    print("... connected from: ", address)
	    print(client)
	    handler = DoctorClientHandler(client)
	    handler.start()
finally:
	#dir(server.shutdown())
	server.close()