import time
from math import radians, cos, sin, asin, sqrt
from datetime import datetime
from datetime import timedelta
from ModulePackage.SMSModule import SMSModule
from ModulePackage.GPSModule import GPSModule
from ModulePackage.SIMModule import SimModule
from ModulePackage.PPPSetup import PPP
from ModulePackage.Settings import Settings
from ModulePackage.Bluetooth import BluetoothPairing
from mpu6050 import mpu6050


def haversine(lon1, lat1, lon2, lat2) -> float:
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # compute great circle distance using the haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # radius of earth in kilometers
    return c * r

def sendMsg(msg: str, phoneNumber: str) -> None:
    sms = SMSModule()
    sms.sendSMS(message=msg, phoneNumber=phoneNumber)
    return None

def getGPS() -> dict:
    gps = GPSModule()
    return gps.get_gps_position()

def calcDisplacement():
    sensor = mpu6050(0x68)
    val1 = sensor.get_accel_data()
    time.sleep(0.5)
    val2 = sensor.get_accel_data()
    return sqrt((val1['x'] - val2['x'])**2 + (val1['y'] - val2['y'])**2 + (val1['z'] - val2['z'])**2)



def main() -> None:
    settings = Settings()
    settings.openSettings()
    bleModule = BluetoothPairing(settings.macAddress)
    bleModule.start()
    module = SimModule("SIM Module")
    module.power_on()
    ppp = PPP()

    
    while ((displacement := calcDisplacement()) < 5 ):
        if (not bleModule.foundDevice and bleModule.bleCounter > 5):
            break
        print(bleModule.bleCounter)
        print(displacement)
        print("waiting for crash")
    bleModule.kill()
    sms = SMSModule()
    sms.sendSMS(message="Car in Motion detected", phoneNumber=settings.phoneNumber)
    journey_id = settings.sendPost("tracking/data/createJourney/", dict(device_id=settings.device_id))
    try:

        while True:
            gps_val1 = getGPS()
            time.sleep(settings.update_journey_interval)
            gps_val2 = getGPS()
            gcd = haversine(gps_val1['longitude'], gps_val1['latitude'], gps_val2['longitude'], gps_val2['latitude'])
            displacement = calcDisplacement()
            settings.sendPost("tracking/data/post/", dict(
                device_id=settings.device_id, username=settings.related_user, journey_id=journey_id, latitude=gps_val2["latitude"], longitude=gps_val2["longitude"],
                gcd=gcd, accelerometer_displacement=displacement

            ))
            time.sleep(settings.texting_timeout)
    except Exception as e:
        module.power_off()
        bleModule.kill()
        print(e)
        ppp.endConnection()

if __name__ == '__main__':
    main()

