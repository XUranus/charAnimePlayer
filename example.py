#!/usr/bin/python
import sys
sys.path.append('./')
from CharAnimeBuilder import *
from CharAnimePlayer import *


#构造灰度字符串
a =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.
                     "
#构造builder 传入视频
builder = CharAnimeBuilder(a,'ikun.mp4') 

#输入宽高 目标持久化文件
builder.build(130,40,'./frames2.dat')

#加载持久化文件 设置帧率(1-60) 初始化播放器
player = CharAnimePlayer.newFramesPlayer('./frames2.dat',20)
#播放
player.play() 