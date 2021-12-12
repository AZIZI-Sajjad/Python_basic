# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:44:08 2021

@author: SDA
"""

import wmi
# Get system procces's Names List
conn = wmi.WMI()
for class_name in conn.classes:
    if 'Process' in class_name:
        print(class_name)

print('*' * 50)
# Get system ressources usages by procces

conn = wmi.WMI()
for process in conn.Win32_Process():
    print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(process.ProcessId, process.HandleCount, process.Name))

# Search a system procces by name  in all procces -> Exemple : "chrome.exe" 
print('#' * 50)
conn = wmi.WMI()
for process in conn.Win32_Process(name="chrome.exe"):
    if process.HandleCount > 1000: # only processes with handle count above 1000
        print(process.ProcessID, process.HandleCount, process.Name)

# Get system users & groups        
print('/' * 50)
conn = wmi.WMI()
for group in conn.Win32_Group():
    print(group.Caption)
for user in group.associators(wmi_result_class="Win32_UserAccount"):
    print(" [+]", user.Caption)
