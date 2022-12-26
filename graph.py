import math
import sys
from datetime import datetime

import ipywidgets as widgets
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as web
from ipywidgets import fixed, interact, interact_manual, interactive
from mplcursors import cursor

path='gps_uart_speed_logs.txt'
file = open(path)  
speeds = []  
timestamps = []  

while True:
    line = file.readline()  
    line = line.replace("\n","")  
    
    if not line or len(line) == 0 or "$GNRMC" not in line:
        break  
    words = line.split(",")  
    date = words[9]  
    time = words[1]  
    date = words[9][0:2] + "/" + words[9][2:4] + "/22"  
    time = words[1][0:2] + ":" + words[1][2:4] + ":" + words[1][4:6]  
    datetime_str = date +" "+ time  
    datetime_obj = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')  

    speed = float(words[7]) * 1.852  
    speeds.append(speed)  
    timestamps.append(datetime_obj)  


plt.plot(timestamps, speeds)  
cursor(hover=True)
plt.show()  

file.close  