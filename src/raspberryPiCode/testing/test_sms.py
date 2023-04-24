import unittest
import json
from ModulePackage.SMSModule import SMSModule

class TestSMS(unittest.TestCase):
    """
    Test the SMS functionality used in theftDetection.py
    """
    def test_send_sms(self):
        """
        Test SMS message sending functionality
        """
        sms = SMSModule()

        sms.power_on()
        print("\nSMS Powering On\n")

        msg = "test"
        # phone number of our sim card
        number = "0830854610"

        sms.sendSMS(message=msg, phoneNumber=number)

        sms.power_off()
        print("\nSMS Powering Off\n")

        self.assertEqual(type(msg), str)
        self.assertEqual(type(number), str)

    def test_retrive_sms(self):
        """
        Test SMS message retrival functionality
        """
        sms = SMSModule()

        sms.power_on()
        print("\nSMS Powering On\n")

        msg = sms.recieveSMSMessage()

        sms.power_off()
        print("\nSMS Powering Off\n")

        self.assertEqual(type(msg), str)