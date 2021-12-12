# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 00:56:37 2021

@author: SDA
"""
# REF :  https://stackoverflow.com/questions/7551546/getting-friendly-device-names-in-python

import wmi
c = wmi.WMI()
wql = "Select * From Win32_USBControllerDevice"
for item in c.query(wql):
    print(item.Dependent.Caption)
