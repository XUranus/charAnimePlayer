#!/usr/bin/python
import cv2
import time
import os
import pickle

class CharAnimeBuilder:
    def __init__(self,ascii_char,filename):
        self.ascii_char = ascii_char#生成一个ascii字符列表
        self.char_len = len(ascii_char)
        self.filename = filename
        
    def build(self,show_width,show_heigth,dst_path):
        vc = cv2.VideoCapture(self.filename)#加载一个视频
        print('processing '+self.filename)
        if vc.isOpened():#正常打开
            rval , frame = vc.read()
        else:
            print('open failed! Abort.')
            exit(1)
        frame_count = 0 #帧数
        outputList = [] #初始化输出列表
        while rval:
            #循环读取视频帧  
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #使用opencv转化成灰度图
            gray = cv2.resize(gray,(show_width,show_heigth))#resize灰度图
            text = ""
            for pixel_line in gray:
                for pixel in pixel_line:                    #字符串拼接
                    text += self.ascii_char[int(pixel / 256 * self.char_len )]
                text += "\n"                                
            outputList.append(text)
            frame_count = frame_count + 1                           
            if frame_count % 100 == 0:
                print(str(frame_count) + " frames processed")
            rval, frame = vc.read()  
        #持久化
        with open(dst_path, 'wb') as f:
            pickle.dump(outputList,f)
        print("compeletd!")
