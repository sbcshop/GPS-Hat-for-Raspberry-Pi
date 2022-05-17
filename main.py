from time import sleep
import sys
import gps_lib

try:
    while 1:
        
        x = gps_lib.RMC_Read() #Recommended minimum specific GNSS data
        if x is not None:
            a = list(x)
            print("Latitude = ",a[0] + "    Longitude = ",a[1])
            print("UTC Time = ",a[2])
            print("Date = ",a[4])
            print("speed over ground = ",a[3])
            print("\n")
        
        y = gps_lib.GSV_Read() # GNSS satellites in view
        if y is not None:
            a = list(y)
            print("Total Number of Satellites = ",a[0])
            print("Satellite ID number = ",a[1])
            print("Elevation = ",a[2])
            print("SNR = ",a[3])
            print("\n")
        
        z = gps_lib.GGA_Read() #Global positioning system (GPS) fix data
        if z is not None:
            a = list(z)
            print(a)
            print("Latitude = ",a[0] + "    Longitude = ",a[1])
            print("UTC Time = ",a[2])
            print("Satellite Positioning = ",a[3])
            print("GPS Quality indicator = ",a[4])
            print("\n")

            
except KeyboardInterrupt:
    sys.exit(0)

