import RPi.GPIO as GPIO
import serial
import time
from ModulePackage.SIMModule import SimModule

class GPSModule(SimModule):
    def __init__(self):
        super().__init__(module="GPS")
    
    def get_gps_position(self) -> dict:
        recNull = True
        answer = False
        print("Starting GPS session....")
        self.recBuff = ""
        if not (self.send_at_command("AT+CGPS?", "1,1", 1)):
            self.send_at_command("AT+CGPS=1,1", "OK", 1)
        while (recNull):
            answer = self.send_at_command("AT+CGPSINFO", "+CGPSINFO: ", 1)
            if answer:
                if ",,,,,," in self.recBuff:
                    print("GPS not ready")
                    time.sleep(1)
                else:
                    recNull = False
                    gpsCode = self.recBuff.partition("+CGPSINFO:")[2].strip()
                    latDM, latDir, longDM, longDir, date, UTCTime, _, _, _ = gpsCode.split(",")
                    latitude = int(latDM[:2]) + (float(latDM[2:]) / 60)
                    longitude = int(longDM[:3]) + (float(longDM[3:]) / 60)
                    if (latDir == "S"):
                        latitude = -latitude
                    if (longDir == "W"):
                        longitude = -longitude
                    day, month, year = ''.join(date[:2]), ''.join(date[2:4]), ''.join(date[4:])
                    hour, minute, second = ''.join(UTCTime[:2]), ''.join(UTCTime[2:4]), ''.join(UTCTime[4:])
        return dict(latitude=latitude, longitude=longitude, DdMmYy=[day, month, year], UTCTime=[hour, minute, second])


 
if __name__ == "__main__":
    gps = GPSModule()
    gps.power_on()
    try:
        gps.get_gps_position()
    except:
        gps.power_off()

