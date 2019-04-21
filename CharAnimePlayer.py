#!/usr/bin/python
import pickle
import os
import time
import platform

class CharAnimePlayer:
    def __init__(self,filepath,fps):
        sysstr = platform.system() #判定系统是linux windows
        if sysstr == "Windows":
            self.clearCommand = "cls"
        elif sysstr == "Linux":
            self.clearCommand = "clear"
            
        self.filepath = filepath
        self.sleepSlot = 1/fps #帧率设置
        with open(self.filepath, 'rb') as f:
            self.frameList = pickle.load(f)


    def play(self):
        for frame in self.frameList:            
            os.system(self.clearCommand)
            print(frame)
            time.sleep(self.sleepSlot)
        os.system(self.clearCommand)
        