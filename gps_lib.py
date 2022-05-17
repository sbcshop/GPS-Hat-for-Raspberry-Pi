import serial              
from time import sleep
import sys
ser = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
buffer = 0
buff = 0

def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position

def GGA_Read():
            data = "$GNGGA,"
            info = data
            received_data = (str)(ser.readline()) #read NMEA string received
            data_available = received_data.find(info)                 
            if (data_available>0):
                buffer = received_data.split(data,1)[1]  #store data coming 
                buff = (buffer.split(','))
                nmea_time = []
                nmea_latitude = []
                nmea_longitude = []
                Sat_positioning = []
                GPS_quality_indicator = []
                GPS_quality_indicator = buff[5]
                nmea_time = buff[0]
                Sat_pos = buff[6]   # satellite position
                nmea_latitude = buff[1]              
                nmea_longitude = buff[3]
                lat = (float)(nmea_latitude)
                lat = convert_to_degrees(lat)
                longi = (float)(nmea_longitude)
                longi = convert_to_degrees(longi)                
                return lat,longi,nmea_time,Sat_pos,GPS_quality_indicator



def RMC_Read():
            data = "$GNRMC,"
            info = data
            received_data = (str)(ser.readline()) #read NMEA string received
            data_available = received_data.find(info)                 
            if (data_available>0):
                buffer = received_data.split(data,1)[1]  #store data coming 
                buff = (buffer.split(','))
                nmea_time = []
                nmea_latitude = []
                nmea_longitude = []
                date = []
                speed_over_ground = []
                nmea_time = buff[0]
                speed_over_ground = buff[6]#extract time from GPGGA string
                nmea_latitude = buff[2]              
                nmea_longitude = buff[4]
                date = buff[8]
                lat = (float)(nmea_latitude)
                lat = convert_to_degrees(lat)
                longi = (float)(nmea_longitude)
                longi = convert_to_degrees(longi)                
                return lat,longi,nmea_time,speed_over_ground,date


def GSV_Read():
            data = "$GLGSV,"
            info = data
            received_data = (str)(ser.readline()) #read NMEA string received
            data_available = received_data.find(info)                  
            if (data_available>0):
                buffer = received_data.split(data,1)[1]  #store data coming 
                buff = (buffer.split(','))
                total_sat = []
                Sat_id = []
                snr = []
                Elevation = []
                total_sat = buff[2]
                Sat_id = buff[3]
                Elev = buff[4]
                snr = buff[6]
                return total_sat,Sat_id,Elev,snr
