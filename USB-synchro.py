# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 00:56:37 2021

@author: SDA
"""

import wmi
import os

"""
c = wmi.WMI()
wql = "Select * From Win32_USBControllerDevice"
for item in c.query(wql):
    print(item.Dependent.Caption)
"""


#PNPDeviceID -> 
#SERIAL NUMBER is included in PNPDeviceID
#☺print("*" * 50, "N° SERIE")

DevicesId = os.popen('wmic diskdrive get SerialNumber ').read()
USB2 = "0415060924000134"
USB1 = "1710162ADB5F"
for Snfinder in DevicesId:
    if USB1 in DevicesId:
        print("USB1 by SN: {} is connected". format(USB1))
    if USB2 in DevicesId:
        print("USB2 by SN: {} is connected". format(USB2))
    break


