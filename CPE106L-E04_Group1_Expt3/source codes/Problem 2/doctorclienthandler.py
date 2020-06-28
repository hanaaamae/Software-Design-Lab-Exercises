"""
File: doctorclienthandler.py
Client handler for providing non-directive psychotherapy.
"""

from codecs import decode
from threading import Thread
from doctor import Doctor

BUFSIZE = 1024
CODE = "ascii"

class DoctorClientHandler(Thread):
    """Handles a session between a doctor and a patient."""
    def __init__(self, client):
        Thread.__init__(self)
        #print(str(client))
        self.client = client
        self.dr = Doctor()
   
    def run(self):
        self.client.send(bytes(self.dr.greeting(self.client),
                               CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE),
                             CODE)
            #print(str(message))
            #ibig sabihin None to?
            if not message:
                #somewhere d2 dapat issave nia ung data ni message
                #print(self.dr.history, self.dr.person)
                #so aun i save mo ung dat file ulit 
                # self.client.send(bytes(self.dr.farewell(), CODE))
                self.dr.updateFile()
                print("Client disconnected")
                self.client.close()
                break
            else:
                #print('yes d2 ako pumasok ok ')
                self.client.send(bytes(self.dr.reply(message),
                                       CODE))


