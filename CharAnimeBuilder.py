#!/usr/bin/python
import cv2
import time
import os
import pickle
import sys

class CharAnimeBuilder:
    def __init__(self,ascii_char,filename):
        self.ascii_char = ascii_char #生成一个ascii字符列表
        self.char_len = len(ascii_char)
        self.filename = filename
        
    def build(self,show_width,show_heigth,dst_path):
        vc = cv2.VideoCapture(self.filename) #加载一个视频
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
            gray = cv2.resize(gray,(show_width,show_heigth)) #resize灰度图
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

def printHelp():
    print("Help:")
    print("\tUsage: python charAnimeBuilder.py <file> [option]")
    print("\tOption:")
    print("\t\t-help \t\tshow help")
    print("\t\t-w -width \tspecify wicth")
    print("\t\t-h -height \tspecify height")
    print("\t\t-arr \tspecify customed char array")
    print("\t\t-o -out \tspecify output *.dat filepath")
    print("\tExample:")
    print("\t\tpython charAnimeBuilder.py bad-apple.mp4 -width 120 -height 35 -o bad-apple.dat")


if __name__=="__main__":
    argv = sys.argv
    i = 1

    # file fps width height
    filepath = ""
    outputpath = ""
    width = -1
    height = -1
    arr =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #default

    #extract command args
    while i < len(argv):
        if argv[i].lower() == "-help":
            printHelp()
            sys.exit(0)
        elif argv[i].lower() == "-w" or argv[i].lower() == "-width":
            if i + 1 < len(argv):
                width = int(argv[i + 1])
                i = i + 1
        elif argv[i].lower() == "-h" or argv[i].lower() == "-height":
            if i + 1 < len(argv):
                height = int(argv[i + 1])
                i = i + 1
        elif argv[i].lower() == "-o" or argv[i].lower() == "-out":
            if i + 1 < len(argv):
                outputpath = argv[i + 1]
                i = i + 1
        elif argv[i].lower() == "-arr":
            if i + 1 < len(argv):
                arr = argv[i + 1]
                i = i + 1
        else:
            filepath = argv[i]
        i = i + 1

    if filepath == "" or outputpath == "" or width < 0 or height < 0 or arr == "":
        printHelp()
        sys.exit(0)

    print("filepath: ",filepath)
    print("height: ",height)
    print("width: ",width)
    print("arr: ",arr)
    print("outpath: ",outputpath)
    
    builder = CharAnimeBuilder(arr, filepath) 
    builder.build(width, height, outputpath) 