import os
import urllib.request

class PPP(object):
    def __init__(self):
        self.state: bool = True

    def determineState(self) -> bool:
        try:
            urllib.request.urlopen("http://google.com")
            return True
        except:
            return False
    def startConnection(self) -> bool:
        os.system("sudo pon rnet")
        print("turning on network")
        return self.state
       
    def endConnection(self) -> bool:
        os.system("sudo poff rnet")
        print("turning off network")
        return self.state