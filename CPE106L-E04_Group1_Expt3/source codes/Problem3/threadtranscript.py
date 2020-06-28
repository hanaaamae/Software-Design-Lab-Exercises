from transcript import Transcript
from sharedcell import SharedCell

class ThreadTranscript:

    def __init__(self, address, chats):
        who = Transcript(address, chats)
        self.cell = SharedCell(who)
    
    def __str__(self):
        return self.cell.read(lambda who: str(who))

    def getChats(self):
        return self.cell.read(lambda who: who.getChats())

    def getAddress(self):
        return self.cell.read(lambda who: who.getAddress())
    
    def addChat(self, message):
        #return self.who.addChat(message)
        return self.cell.write(lambda who: who.addChat(message))
        