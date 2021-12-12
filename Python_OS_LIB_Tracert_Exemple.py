# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 00:56:37 2021

@author: SDA
"""

import os
print("#" * 50, "TRACERT")
TRACERT = os.popen('tracert 8.8.8.8').read()
print(TRACERT)
