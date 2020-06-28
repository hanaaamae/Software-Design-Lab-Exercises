from codecs import decode
from threading import Thread
from threadtranscript import ThreadTranscript

BUFSIZE = 1024
CODE = "ascii"

class ChatClientHandler(Thread):
    #Handles session between server and client
    def __init__(self, client, address):
        Thread.__init__(self)
        self.client = client
        self.address = address
        #self.ls = []
        self.trans = ThreadTranscript(self.address[1], "Connected")
   
    def run(self):
        #self.client.send(bytes("You have connected to the server!", CODE))
        self.client.send(bytes(str(self.trans.getChats()), CODE))
        
        while True:
            message = decode(self.client.recv(BUFSIZE), CODE)
            self.trans.addChat([self.address[1], message])
            #Ui_MainWindow().windowRefresh()
            #ThreadTranscript().addChat([self.address[1], message])
            #ls = "%s: %s" % (str(self.address[1]), self.trans.getChats())
            #ls = "%s: %s" % (self.trans.getAddress(), self.trans.getChats())
            if not message:
                #self.client.send(bytes("Client %s disconnected" % str(self.address[1]),CODE))
                print("Client %s disconnected from the server" % str(self.address[1]))
                #print(self.trans.getChats())
                #self.trans.rmChat()
                self.client.close()
                break
            else:
                self.client.send(bytes(str(self.trans.getChats()), CODE))
                print(self.trans.getChats())
                