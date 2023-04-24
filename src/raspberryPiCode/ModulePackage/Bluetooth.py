import bluetooth as ble
import threading

class BluetoothPairing(object):
    def __init__(self, authorizedMacAddress):
        self.authorizedMacAddress = authorizedMacAddress
        self.bleCounter = 0
        self.devicesInRange = []
        self.running = False
        self.foundDevice = False
    
    def searchForBle(self):
        while (self.running):
            self.devicesInRange = ble.discover_devices(duration=5, flush_cache=True, lookup_names = True, lookup_class = True)
            self.bleCounter += 1
            for device in self.devicesInRange:
                if (any(item in self.authorizedMacAddress for item in device)):
                    self.foundDevice = True
                    self.bleCounter = 0
                    break

        
    def start(self):
        self.running = True
        findDevice = threading.Thread(target=self.searchForBle)
        findDevice.start()

    def kill(self):
        self.running = False
    
if __name__ == '__main__':
    bluet = BluetoothPairing(["64:A2:00:58:56:57"])
    bluet.start()