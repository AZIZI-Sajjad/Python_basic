# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 00:56:37 2021

@author: SDA
"""
# REF : https://forum.micropython.org/viewtopic.php?f=17&t=7509
# Python 3.8 
# OS Windows 10
import wmi
import os
c = wmi.WMI()
wql = "Select * From Win32_USBControllerDevice"
for item in c.query(wql):
    print(item.Dependent.Caption)
