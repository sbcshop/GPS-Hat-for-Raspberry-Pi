# GPS-Hat-for-Raspberry-Pi

<img src= "https://github.com/sbcshop/GPS-Hat-for-Raspberry-Pi/blob/main/images/img0.jpg" />

### The extremely compact and powerful GNSS module GPS HAT for Pi is a concurrent receiver module that integrates GPS with the BeiDou system. It's pin-to-pin compatible with Quectel's GNSS module L76 and can receive both GPS and BeiDou open service L1 signals at the same time. GPS HAT for Pi can acquire and track any mix of GPS and BeiDou signals thanks to its 33 tracking channels, 99 acquisition channels, and 210 PRN channels. When compared to utilizing simply GPS, enabling both GPS and BeiDou doubles the number of visible satellites, reduces the time to first fix, and improves positioning accuracy, especially in congested urban areas.

<img src= "https://github.com/sbcshop/GPS-Hat-for-Raspberry-Pi/blob/main/images/img1.JPG" />

## Before code run, check PPS led is blinking or not, it takes time approx 10 to 20 sec,and place anteena outside the house for better connection

## Device Features
 * Supports Multi-GNSS systems: GPS, BDS, and QZSS
 * UART communication baudrate: 4800~115200bps and 9600bps is default
 * Four Led's for indicating the module working status
 * UART selection jumper wire(A,B and C)
 * Onboard battery holder
 
## General Specifications
 * Protocols- NMEA 0183, PMTK
 * Operating current: 13mA
 * Power supply voltage: 5V / 3.3V
 * Operating temperature: -40℃ to 85℃
  

## Components

<img src= "https://github.com/sbcshop/GPS-Hat-for-Raspberry-Pi/blob/main/images/img2.jpg" />

### **1.UART Selection Jumper**

A - USB-L76X module ( Using USB TO UART, control the L76X)

B - PI - L76X module (control the L76X through Raspberry Pi)

C - USB -PI ( access Raspberry Pi through USB TO UART)

### **2.Standby Switch**

The Standby switch is used to toggle between Standby and Working modes. The power consumption of the module in standby mode is quite low. It disables satellite navigation and search.


### **3.Backup Mode ON Button ( Force ON Button)**

To exit Backup mode, press the FORCE ON button.


### **4.Battery Holder**
For maintaining ephemeris data and hot starts, there is an onboard battery holder that supports the ML1220 battery.



### **5.Indicators:**

a) RXD/TXD: UART RX/TX indicator

b) PPS: GPS status indicator (if your PPS light is blinking it means your module is receiving GPS signal)

c) PWR: power indicator of HAT


### **NMEA-Format**

**This protocol is based on the international standard for maritime navigation and radio communication, equipment and systems and digital interfaces (IEC 61161-1). This standard adopted the de-facto standards for interfacing marine electronic devices, known as NMEA 0183.
The data is transmitted in sentences of variable length with a specified sentence structure.**

For eg- (OUTPUT)

$GNGGA,185833.80,4808.7402397,N,01133.9325039,E,5,15,1.1,470.50,M,45.65,M,,*75

$GNVTG,112.99,T,109.99,M,0.15,N,0.08,K,A*3B

$GNGSA,2,M,06,12,15,17,19,24,25,32,1.34,0.96,0.93*1D



### Sentence structure
* Address field
* Data fields
* Checksum field
* Terminating field
* All sentences contain only ASCII characters
* The maximum length of a sentence is 82 characters
* All fields are separated by delimiters

### Address field
The address field starts with “$” followed by the talker ID and a sentence identifier. The used talker IDs are:
* GP for GPS only solutions
* GL for GLONASS only solutions
* GN for multi GNSS solutions

### The used sentence identifiers are:
* GGA – Global Positioning System Fix Data
* VTG – Course over Ground and Ground Speed
* GSA – GNSS DOP and Active Satellites
* GSV – GNSS Satellites in View
* RMC – Recommended Minimum Specific GNSS Data


### Data fields
Data fields must always be separated by “,”. They can contain alpha, numeric and alphanumeric values all coded in ASCII characters. The length of a data field can be constant, variable or can contain a fixed and variable portion. This differs for each sentence.

### Checksum field
The Checksum field starts with “*” followed by the checksum of the sentence.
The Checksum is generated with a bitwise exclusive OR of all fields including the “,” delimiters, between but not including the “$” and the “*” characters.
The hexadecimal value of the checksum is then converted to two ASCII characters.

### Terminating field
The terminating sequence contains the two ASCII characters <CR> and <LF> without any delimiter.

### Satellite Numbering
  
 GPS: 1-32
  
 GLONASS: 33-96

  
 ## Code
 
 **gps_lib.py**      - library of gps 
  
 **gps_raw_data.py** - Run this file to receive gps raw data
  
 **google_map.py**   - Run this file to show your location on google map
  
 **main.py**         - Run the file to know location, number of satellite, altitude , speed etc
 
 ## GPS HAT Getting Started Video
 https://www.youtube.com/watch?v=h0ZOMqL_U-c&ab_channel=SBComponentsLtd
