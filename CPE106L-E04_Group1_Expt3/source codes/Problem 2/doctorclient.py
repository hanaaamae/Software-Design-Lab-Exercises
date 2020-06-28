"""
File: doctorclient.py
GUI-based view for client for non-directive psychotherapy.
"""

#fix textbox at start to avoid confusion

from socket import *
from codecs import decode
from breezypythongui import EasyFrame

HOST = "localhost"
PORT = 4321
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

class DoctorClient(EasyFrame):
    """Represents the client's window."""

    COLOR = "#CCEEFF"      # Light blue

    def __init__(self):
        """Initialize the window and widgets."""
        EasyFrame.__init__(self, title = "Doctor",
                           background = DoctorClient.COLOR)

        self.name = ''

        # Add the labels, fields, and button
        self.drLabel = self.addLabel(text = "Want to connect?",
                                     row = 0, column = 0,
                                     columnspan = 2,
                                     background = DoctorClient.COLOR)
        self.ptField = self.addTextField(text = "", row = 1,
                                         column = 0,
                                         columnspan = 2,
                                         width = 50,
                                         state='disabled')
        self.sendBtn = self.addButton(row = 2, column = 0,
                                      text = "Send reply",
                                      command = self.sendReply,
                                      state = "disabled")
        self.connectBtn = self.addButton(row = 2, column = 1,
                                      text = "Connect",
                                      command = self.connect)
        
        # Support the return key in the input field
        self.ptField.bind("<Return>", lambda event: self.sendReply())

    def sendReply(self):
        """Sends patient input to doctor, and receives
        and outputs doctor's reply."""

        ptInput = self.ptField.getText()
        if ptInput != "":
            self.server.send(bytes(ptInput, CODE))
            #print(self.server.recv(BUFSIZE))

            drReply = decode(self.server.recv(BUFSIZE), CODE)
            
            if not drReply:
                self.messageBox(message = "Doctor disconnected")
                self.disconnect()
            else:
                self.drLabel["text"] = drReply
                self.ptField.setText("")
            
    def connect(self):
        """Starts a new session with the doctor."""
        #print(self.drLabel['text'])
        self.server = socket(AF_INET, SOCK_STREAM)
        #print(self.server)
        self.server.connect(ADDRESS)
        # print(BUFSIZE)
        #print(self.server.recv(BUFSIZE))
        #self.name = self.ptField.getText()
        #print(self.name)
        self.drLabel["text"] = decode(self.server.recv(BUFSIZE), CODE)
        #print(self.drLabel['text'])

        self.connectBtn["text"] = "Disconnect"
        self.connectBtn["command"] = self.disconnect
        self.sendBtn["state"] = "normal"
        self.ptField['state'] = 'normal'
            
    def disconnect(self):
        """Ends the session with the doctor."""
        #self.ptField.setText(decode(self.server.recv(BUFSIZE), CODE))
        self.server.close()
        self.ptField.setText('')
        self.drLabel["text"] = "Want to connect?"
        self.connectBtn["text"] = "Connect"
        self.connectBtn["command"] = self.connect
        self.sendBtn["state"] = "disabled"
        self.ptField['state'] = 'disabled'

def main():
    """Instantiate and pop up the window."""
    DoctorClient().mainloop()

if __name__ == "__main__":
    main()



