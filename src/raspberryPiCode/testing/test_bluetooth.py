import unittest
import bluetooth


class TestBluetooth(unittest.TestCase):
    """
    Test the bluetooth functionality used in theftDetection.py
    """
    def test_scan(self):
        """
        Test the scan function which returns all bluetooth devices in range
        """
        devicesInRange = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
        self.assertEqual(type(devicesInRange), list)
    
    def test_data(self):
        """
        Test the data received from reading bluetooth sample file
        """
        with open("./bluetoothData.txt", "r") as bluetoothData:
        
            devicesData = bluetoothData.readlines()
        
        self.assertEqual(devicesData[0], ('64:A2:00:58:56:57', 'Mi 10T Lite', 5898764))

if __name__ == '__main__':
    unittest.main()