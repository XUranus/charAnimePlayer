#!/usr/bin/python
import sys
sys.path.append('./')
from CharAnimeBuilder import *
from CharAnimePlayer import *


#构造灰度字符串
a =  "@@@@@@@@@*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?                                          "
#构造builder 传入视频
builder = CharAnimeBuilder(a,'/home/xuranus/Desktop/ikun/ikun.mp4') 
#输入宽高 目标持久化文件
builder.build(130,40,'./f.dat')


#加载持久化文件 设置帧率(1-60) 初始化播放器
player = CharAnimePlayer('./f.dat',10)
#播放
player.play()