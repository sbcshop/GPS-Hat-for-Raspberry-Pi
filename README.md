# GPS-Hat-for-Raspberry-Pi

<img src= "https://github.com/sbcshop/GPS-Hat-for-Raspberry-Pi/blob/main/images/img0.jpg" />

### The extremely compact and powerful GNSS module GPS HAT for Pi is a concurrent receiver module that integrates GPS with the BeiDou system. It's pin-to-pin compatible with Quectel's GNSS module L76 and can receive both GPS and BeiDou open service L1 signals at the same time. GPS HAT for Pi can acquire and track any mix of GPS and BeiDou signals thanks to its 33 tracking channels, 99 acquisition channels, and 210 PRN channels. When compared to utilizing simply GPS, enabling both GPS and BeiDou doubles the number of visible satellites, reduces the time to first fix, and improves positioning accuracy, especially in congested urban areas.

<img src= "https://github.com/sbcshop/GPS-Hat-for-Raspberry-Pi/blob/main/images/img1.JPG" />

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

Power Backup


### **5.Indicators:**

a) RXD/TXD: UART RX/TX indicator

b) PPS: GPS status indicator

c) PWR: power indicator of HAT

## Code

