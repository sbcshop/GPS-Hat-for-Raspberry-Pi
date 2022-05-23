# Receive Raw GPS Data
import RPi.GPIO as GPIO
import time
import serial


#serial interface
gps_module = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
try:
    while 1:
        data_Read = gps_module.readline()#read data comming from other pi lora Hat
        print(data_Read)

        
except KeyboardInterrupt:
    GPIO.cleanup()
