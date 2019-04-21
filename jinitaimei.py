#!/usr/bin/python
import sys
sys.path.append('./')
from CharAnimePlayer import *

player = CharAnimePlayer('./frames.dat',10)
player.play()