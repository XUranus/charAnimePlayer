#!/usr/bin/python
import pickle
import os
import time
import platform
import sys


class CharAnimePlayer:
    def __init__(self,mode,filepath,fps,show_width,show_height):
        sysstr = platform.system() #判定系统是linux windows
        if sysstr == "Windows":
            self.clear_command = "cls"
        elif sysstr == "Linux":
            self.clear_command = "clear"
        else:
            print("unknown platform: ",sysstr)
            sys.exit(0)
        self.show_height = show_height
        self.show_width = show_width
        self.mode = mode #charsFrames|rawVideo
        self.filepath = filepath
        self.sleep_slot = 1/fps #帧率设置

    def play(self,has_audio = False):
        if(self.mode=="charsFrames"):
            with open(self.filepath, 'rb') as f:
                self.frame_list = pickle.load(f)
            self.play_frames()
        elif(self.mode=="rawVideo"):
            self.play_raw(self.show_width,self.show_height,has_audio)

    def play_frames(self):
        for frame in self.frame_list:            
            os.system(self.clear_command)
            print(frame)
            time.sleep(self.sleep_slot)
        os.system(self.clear_command)
        
    def play_raw(self,show_width,show_height,has_audio):
        import cv2
        self.ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        self.char_len = len(self.ascii_char)
        vc = cv2.VideoCapture(self.filepath)#加载一个视频
        if vc.isOpened():#正常打开
            rval , frame = vc.read()
        else:
            print('open failed! Abort.')
            exit(1)
        if has_audio: #声音
            import moviepy.editor as me
            import pygame
            sound = me.VideoFileClip(self.filepath).audio #sound from a video
            soundArray = sound.write_audiofile("tmp.wav") #convert to NumPy array
            pygame.mixer.init()
            pygame.mixer.music.load("tmp.wav")
            os.system(self.clear_command)
            pygame.mixer.music.play()
        while rval:
            #循环读取视频帧  
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #使用opencv转化成灰度图
            gray = cv2.resize(gray,(show_width,show_height))#resize灰度图
            text = ""
            for pixel_line in gray:
                for pixel in pixel_line:                    #字符串拼接
                    text += self.ascii_char[int(pixel / 256 * self.char_len )]
                text += "\n"    
            os.system(self.clear_command)                            
            print(text)
            time.sleep(self.sleep_slot)
            rval, frame = vc.read()  
        os.system(self.clear_command)
        print("play finished.")


def newFramesPlayer(filepath,fps):
    return CharAnimePlayer("charsFrames",filepath,fps,-1,-1)

def newRawPlayer(filepath,fps,show_width,show_height):
    return CharAnimePlayer('rawVideo',filepath,fps,show_width,show_height)

def printHelp():
    print("Help:")
    print("\tUsage: python charAnimePlayer.py <file> [option]")
    print("\tOption:")
    print("\t\t-help \t\tshow help")
    print("\t\t-w -width \tspecify wicth")
    print("\t\t-h -height \tspecify height")
    print("\t\t-f -fps \tspecify fps from 1 to 60")
    print("\t\t--raw \t\traw play model")
    print("\t\t--audio \tplay with audio")
    print("\tExample:")
    print("\t\tpython charAnimePlayer.py bad-apple.mp4 - fps 60 -width 120 -height 35 --audio --raw")
    print("\t\tpython charAnimePlayer.py jinitaimei1.dat - fps 60")


if __name__=="__main__":
    argv = sys.argv
    i = 1
    
    # file fps width height
    filepath = ""
    width = -1
    height = -1
    fps = -1
    player_type = "frames" # frames or raw
    has_audio = False
    player = None

    #extract command args
    while i < len(argv):
        if argv[i].lower() == "-help":
            printHelp()
            sys.exit(0)
        elif argv[i].lower() == "--raw":
            player_type = "raw"
        elif argv[i].lower() == "--audio":
            has_audio = True
        elif argv[i].lower() == "-w" or argv[i].lower() == "-width":
            if i + 1 < len(argv):
                width = int(argv[i + 1])
                i = i + 1
        elif argv[i].lower() == "-h" or argv[i].lower() == "-height":
            if i + 1 < len(argv):
                height = int(argv[i + 1])
                i = i + 1
        elif argv[i].lower() == "-f" or argv[i].lower() == "-fps":
            if i + 1 < len(argv):
                fps = int(argv[i + 1])
                i = i + 1
        else:
            filepath = argv[i]
        i = i + 1

    if player_type == "frames":
        if filepath == "" or fps < 0:
            printHelp()
            sys.exit(0)
    elif player_type == "raw":
        if filepath == "" or fps < 0 or width < 0 or height < 0:
            printHelp()
            sys.exit(0)


    if player_type == "raw":
        print("mode: ", player_type)
        print("filepath: ",filepath)
        print("fps: ",fps)
        print("height: ",height)
        print("width: ",width)
        print("audio On: ", has_audio)
        player = newRawPlayer(filepath, fps, width, height)
    else:
        print("mode: ", player_type)
        print("filepath: ",filepath)
        print("fps: ",fps)
        player = newFramesPlayer(filepath, fps)

    player.play(has_audio)
