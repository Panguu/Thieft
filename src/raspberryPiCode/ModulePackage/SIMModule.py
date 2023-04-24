import RPi.GPIO as GPIO
import serial
import time
from dataclasses import dataclass, field

@dataclass
class SimModule(object):
    serial: any = field(init=False, default=serial.Serial('/dev/ttyS0', 115200))
    powerKey: int = field(init=False, repr=False, default=6)
    module: str = 'SimModule'
    recBuff: str = field(init=False, repr=False, default='')

    def __post_init__(self):
        self.serial.flushInput()
    
    def power_off(self) -> True:
        print("powering off")
        try:
            GPIO.output(self.powerKey, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(self.powerKey, GPIO.LOW)
            time.sleep(5)
            print("Powered Off")
            return True
        except:
            return False
    
    def power_on(self) -> bool:
        print("powering on")
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.powerKey, GPIO.OUT)
            time.sleep(0.1)
            GPIO.output(self.powerKey, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.powerKey, GPIO.LOW)
            time.sleep(5)
            self.serial.flushInput()
            print("powered on")
            return True
        except:
            return False
    
    def send_at_command(self, command: str, back: str, timeout: int) -> bool:
        self.recBuff = ""
        self.serial.write((command+'\r\n').encode())
        time.sleep(timeout)
        if self.serial.inWaiting():
            time.sleep(0.01)
            self.recBuff = self.serial.read(self.serial.inWaiting()).decode()
        if self.recBuff != "":
            if back not in self.recBuff:
                print(f"{command}: Run Error")
                print(f"{command}: returned : {self.recBuff}")
                return False
            else:
                return True
        else:
            print(f"{self.module} not ready")
            return False

    def reset(self) -> None:
        self.sent_at_command("AT+CRESET", "OK", 10)
    

