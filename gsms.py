# send sms via gsm module
import serial
import RPi.GPIO as GPIO
import os
import time
import unittest

# 1: Module set-up
# Enable Serial Communication
port = serial.Serial("/dev/serial0", 9600, timeout=1.0, write_timeout=10)

print(port)

def text(message):
    """ Send text messages to recipient phone number """
    # helpers
    # '\r' indicates ENTER key
    def _status():
        ''' reads and prints port status, then sleep for 1 second '''
        # print(port.read(10))
        # time.sleep(5)
        while True:
            response = port.readline()
            print(response)
            if 'OK' in response:
                break

    # 2: Begin
    # port.flushOutput()
    # port.flushInput()
    port.write('AT\r')
    _status()

    # Disable Echo
    port.write('ATE0\r')
    _status()

    # Set Message format to Text mode
    port.write('AT+CMGF=1\r')
    _status()

    # Set Message Source number
    # port.write('AT+CMSC="+254718414613"\r')
    # _status()

    # Set Message Recipient number
    port.write('AT+CMGS="+254700595009"\r')
    _status()

    # Send message
    port.write(message + '\x1A')
    _status()

    # Enable sendign sms
    port.write('\x1A')
    _status()

    return ('OK' in port.readline())

class TestSendText(unittest.TestCase):
    message = '01001000 01100101 '
    def test_send_text(self):
        self.assertTrue(text(self.message))

if __name__ == '__main__':
    unittest.main()
