#!/usr/bin/python
import sys
sys.path.append('./')
from CharAnimePlayer import *

player = CharAnimePlayer.newFramesPlayer('./frames2.dat',10)
player.play()