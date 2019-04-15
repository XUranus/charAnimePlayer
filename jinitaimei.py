#!/usr/bin/python
import pickle
import os
import time

with open('./frames.dat', 'rb') as f:
    frameList = pickle.load(f)
    for frame in frameList:            
        os.system("clear")
        print(frame)
        time.sleep(0.1)

os.system("clear")