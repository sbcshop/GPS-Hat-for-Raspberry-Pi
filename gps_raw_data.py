#!/usr/bin/env python3

# Receive Raw GPS Data
import time
import serial


# serial interface
gps_module = serial.Serial(
    port="/dev/serial0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)
try:
    while 1:
        data_Read = gps_module.readline()  # read data
        print(data_Read)


except KeyboardInterrupt:
    sys.exit(0)
