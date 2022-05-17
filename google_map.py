import serial              
from time import sleep
import sys
import gps_lib
import webbrowser

try:
    while 1:
        x = gps_lib.GGA_Read()
        if x is not None:
            a = list(x)
            print("Latitude = ",a[0] + "    Longitude = ",a[1])
            map_link = 'http://maps.google.com/?q=' + a[0] + ',' + a[1]
            
except KeyboardInterrupt: # press control + c to open map
    webbrowser.open(map_link)
    sys.exit(0)
