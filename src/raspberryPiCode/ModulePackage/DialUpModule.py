import RPi.GPIO as GPIO
import serial
import time
from SIMModule import SimModule

class DialUpModule(SimModule):
    def __init__(self):
        super().__init__(module="DialUp")
        self.APN = "internet"
        self.serverIP = "http://10.20.1.42"
        self.port = "80"
    
    def postRequest(self, data):
        self.send_at_command('AT+CSQ','OK',1)
        self.send_at_command('AT+CREG?','+CREG: 0,1',1)
        self.send_at_command('AT+CPSI?','OK',1)
        self.send_at_command('AT+CGREG?','+CGREG: 0,1',0.5)
        self.send_at_command('AT+CGSOCKCONT=1,\"IP\",\"'+self.APN+'\"','OK',1)
        self.send_at_command('AT+CSOCKSETPN=1', 'OK', 1)
        self.send_at_command('AT+CIPMODE=0', 'OK', 1)
        self.send_at_command('AT+NETOPEN', '+NETOPEN: 0',5)
        self.send_at_command('AT+IPADDR', '+IPADDR:', 1)
        self.send_at_command('AT+CIPOPEN=0,\"TCP\",\"'+self.serverIP+'\",'+self.port,'+CIPOPEN: 0,0', 5)
        self.send_at_command('AT+CIPSEND=0,', '>', 2)#If not sure the message number,write the command like this: AT+CIPSEND=0, (end with 1A(hex))
        self.serial.write(data.encode())
        if 1 == self.send_at_command(b'\x1a'.decode(),'OK',5):
            print('send message successfully!')
        self.send_at_command('AT+CIPCLOSE=0','+CIPCLOSE: 0,0',15)
        self.send_at_command('AT+NETCLOSE', '+NETCLOSE: 0', 1)

if __name__ == '__main__':
    d = DialUpModule()
    d.power_on()
    d.postRequest('{"name": "SUGMA"}')
    d.power_off()
# AT+HTTPPARA="URL","website.com"
# AT+HTTPPARA="USERDATA","KEY=VALUE&KEY=VALUE"
# AT+HTTPACTION=2 #this says submit as a POST request
# AT+HTTPREAD #returns the reply from the server