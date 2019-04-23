#!/usr/bin/python
import pickle
import os
import time
import platform
import sys

class CharAnimePlayer:
    def __init__(self,mode,filepath,fps,show_width,show_heigth):
        sysstr = platform.system() #判定系统是linux windows
        if sysstr == "Windows":
            self.clearCommand = "cls"
        elif sysstr == "Linux":
            self.clearCommand = "clear"
        self.show_heigth = show_heigth
        self.show_width = show_width
        self.mode = mode
        self.filepath = filepath
        self.sleepSlot = 1/fps #帧率设置

    def newFramesPlayer(filepath,fps):
        return CharAnimePlayer("charsFrames",filepath,fps,-1,-1)
    
    def newRawPlayer(filepath,fps,show_width,show_heigth):
        return CharAnimePlayer('rawVideo',filepath,fps,show_width,show_heigth)

    def play(self):
        if(self.mode=="charsFrames"):
            with open(self.filepath, 'rb') as f:
                self.frameList = pickle.load(f)
            self.playFrames()
        elif(self.mode=="rawVideo"):
            self.playRaw(self.show_width,self.show_heigth)

    def playFrames(self):
        for frame in self.frameList:            
            os.system(self.clearCommand)
            print(frame)
            time.sleep(self.sleepSlot)
        os.system(self.clearCommand)
        
    def playRaw(self,show_width,show_heigth):
        import cv2
        self.ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        self.char_len = len(self.ascii_char)
        vc = cv2.VideoCapture(self.filepath)#加载一个视频
        if vc.isOpened():#正常打开
            rval , frame = vc.read()
        else:
            print('open failed! Abort.')
            exit(1)
        while rval:
            #循环读取视频帧  
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #使用opencv转化成灰度图
            gray = cv2.resize(gray,(show_width,show_heigth))#resize灰度图
            text = ""
            for pixel_line in gray:
                for pixel in pixel_line:                    #字符串拼接
                    text += self.ascii_char[int(pixel / 256 * self.char_len )]
                text += "\n"    
            os.system(self.clearCommand)                            
            print(text)
            time.sleep(self.sleepSlot)
            rval, frame = vc.read()  
        os.system(self.clearCommand)
        print("play finished.")

if __name__=="__main__":
    player = CharAnimePlayer.newRawPlayer(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
    player.play()