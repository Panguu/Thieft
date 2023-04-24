from django.test import TestCase

from .models import BluetoothDevice, DeviceSettings

class BluetoothDeviceTestCase(TestCase):
    
    def setUp(self):
        """test for BluetoothDevice object"""
        BluetoothDevice.objects.create(id="1", name='testDevice1', mac_address='64:A2:00:58:56:57')
        BluetoothDevice.objects.create(id="2", name='testDevice2',mac_address='F8:77:B8:62:78:4B')


    def testMAC(self):
        """test for BluetoothDevice MAC Address"""
        BluetoothDevice1 = BluetoothDevice.objects.get(name='testDevice1')
        BluetoothDevice2 = BluetoothDevice.objects.get(name='testDevice2')

        self.assertEqual(BluetoothDevice1.mac_address, '64:A2:00:58:56:57')
        self.assertEqual(BluetoothDevice2.mac_address, 'F8:77:B8:62:78:4B')
    

    def testID(self):
        """test for BluetoothDevice ID"""
        BluetoothDevice1 = BluetoothDevice.objects.get(name='testDevice1')
        BluetoothDevice2 = BluetoothDevice.objects.get(name='testDevice2')

        self.assertEqual(BluetoothDevice1.id, 1)
        self.assertEqual(BluetoothDevice2.id, 2)

class DeviceSettingsTestCase(TestCase):
    
    def setUp(self):
        """test for DeviceSettings object"""
        DeviceSettings.objects.create(user_id='1', texting_timeout=3000, update_journey_interval=6000)
        DeviceSettings.objects.create(user_id='2', texting_timeout=1000, update_journey_interval=2000)
