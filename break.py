# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import webbrowser
import time 

counter = 0
while counter < 3:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=2Vss3avr0cs")
    counter = counter + 1
