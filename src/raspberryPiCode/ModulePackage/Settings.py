from dataclasses import dataclass, field
import json
from requests import post, get
from ModulePackage.PPPSetup import PPP
import time
import os

@dataclass
class Settings:
    device_id: int = ""
    related_user: str = ""
    url: str = ""
    settings_location: str = os.getcwd() + "/settings.json"
    ppp: PPP = field(init=False, default=PPP())
    texting_timeout: int = 30
    update_journey_interval: int = 30
    
    def openSettings(self):
        with open(self.settings_location) as sf:
            parseJson = json.load(sf)
            self.device_id = parseJson["device_id"]
            self.related_user = parseJson["relatedUser"]
            self.url = parseJson["url"]
            self.macAddress = parseJson["macAddress"]
        self.retriveSettingsFromServer()
    
    def retriveSettingsFromServer(self):
        self.ppp.startConnection()
        time.sleep(5)
        retrived = get(f"{self.url}/tracking/data/getSettings/{self.device_id}", verify=False)
        try:
            retrived = json.loads(retrived.text)
            self.texting_timeout = retrived["texting_timeout"]
            self.phoneNumber = retrived["phoneNumber"]
            self.update_journey_interval = retrived["update_journey_interval"]
            self.macAddress = retrived["registeredBluetoothDevices"]
        except:
            print("No settings found")
        time.sleep(5)
        self.ppp.endConnection()
        return retrived.text
    
    def sendPost(self, pathname, postItems):
        self.ppp.startConnection()
        time.sleep(5)
        print(f"{self.url}/{pathname}")
        retrived = post(f"{self.url}/{pathname}", json=json.loads(str(postItems).replace("'", '"')), verify=False)
        time.sleep(5)
        self.ppp.endConnection()
        return retrived.text
    
        
