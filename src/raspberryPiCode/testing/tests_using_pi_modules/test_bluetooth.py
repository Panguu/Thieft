import unittest
import bluetooth

class TestBluetooth(unittest.TestCase):
    """
    Tests for bluetooth module on raspberry pi
    """
    def test_scan(self):
        """
        Test needs at least one bluetooth device to be in range
        - this is to ensure that the device takes in a tuple for each bluetooth device
        """
        devicesInRange = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
        self.assertEqual(type(devicesInRange), list)
        self.assertEqual(type(devicesInRange[0]), tuple)
    
if __name__ == '__main__':
    unittest.main()