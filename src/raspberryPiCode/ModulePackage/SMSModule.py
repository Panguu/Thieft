import RPi.GPIO as GPIO
import serial
import time
from ModulePackage.SIMModule import SimModule

class SMSModule(SimModule):
    def __init__(self):
        super().__init__("SMSModule")
    
    def sendSMS(self, message: str, phoneNumber: str):
        print("Entering SMS Mode")
        self.send_at_command("AT+CMGF=1", "OK", 1)
        answer = self.send_at_command(f'AT+CMGS=\"{phoneNumber}\"', ">", 2)
        if answer:
            self.serial.write(message.encode())
            self.serial.write(b'\x1A')
            answer = self.send_at_command("", "OK", 8)
            if answer:
                print("Sent Sucessfully")
            else:
                print(f"Error sending message:{answer}")
        else:
            print(f"Error {answer}")
    
    def recieveSMSMessage(self):
        self.recBuff = ""
        print("Setting SMS Mode")
        self.send_at_command("AT+CMGF=1", "OK", 1)
        self.send_at_command('AT+CPMS=\"SM\",\"SM\",\"SM\"', "OK", 1) 
        answer = self.send_at_command("AT+CMGR=1", "+CMGR:", 2)
        if answer:
            answer = False
            if "OK" in self.recBuff:
                answer = True
                print(self.recBuff)
        else:
            print(f"Error: {answer}")
            return f"Error: {answer}"
        return self.recBuff

if __name__ == "__main__":
    sms = SMSModule()
    sms.power_on()
    sms.sendSMS(message="Test", phoneNumber="0868499640")
    sms.power_off()
