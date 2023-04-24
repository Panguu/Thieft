import unittest
import json
from ModulePackage.GPSModule import GPSModule

class TestGPS(unittest.TestCase):
    """
    Test the GPS functionality used in theftDetection.py
    """
    def test_sample_data(self):
        """
        Test sample GPS data
        """
        # open file containing sample GPS data
        streamData = []
        with open("./testing/gpsData.txt", "r") as gpsData:
        # store data in list
            for line in gpsData.readlines():
                data = json.loads(line.replace("\'", "\""))
                streamData.append(data)
        
        for item in streamData:
            self.assertEqual(type(item), dict)
    
    def test_gps(self):
        """
        Test GPS get_gps_position()
        """
        gps = GPSModule()

        print("GPS Powering On")
        gps.power_on()

        try:
            sample = gps.get_gps_position()
        except:
            print("GPS Powering Off")
            gps.power_off()
        
        self.assertEqual(type(sample), dict)
        self.assertEqual(type(sample['latitude']), str)