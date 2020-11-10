# CharAnimePlayer
用opencv读取视频帧，压缩，构造灰度字符串，用字符串替换像素。实现在终端播放字符动画。

## 安装
需要:
 - python3
 - opencv
 - pygame
 - moviepy

安装：
`sudo pip install -r requirements.txt`

## 样例
在终端播放“鸡你太美”
```bash
python charAnimePlayer.py jinitaimei2.dat -fps 20 #每秒20帧
```
效果如下：
![](demo.gif)


## 即时播放
播放指定的**mp4**文件：
```bash
python charAnimePlayer.py <file> [option]
```
选项:`-width`,`-height`,`-fps`设置宽高与帧率，还需带上`--raw`。

Bad Apple样例（50帧，宽70字符，高35字符）:
```
python charAnimePlayer.py -fps 50 -width 70 -height 35 bad-apple.mp4 --raw
```
![](demo2.gif)

> 当附带`--audio`选项时，可以开启声音（**尚未解决音画同步的问题**）。

> **该种播放方式是一边转化每一帧为灰度字符串，一边播放，配置不行电脑的可能会卡**。建议用该种模式调试适合你的屏幕的宽高以及帧率，然后选用下面**预处理播放**的方式获得更流畅的体验。

> `fps`,`width`,`height`需要根据自己的电脑调试。`fps`设置在1-60内，`width`和`height`是指宽高的字符数，建议不要超过100

## 预处理播放
为解决即时播放的卡顿问题，可以使用预处理播放。预处理后生成的预处理文件不需要依赖其他库也能播放。

对于一个`bad-apple.mp4`文件预处理播放的方式如下:
```
python3 charAnimeBuilder.py bad-apple.mp4 -width 100 -height 100 -o bad-apple.dat
```
预处理需要设置宽高，输出路径。完成后会生成`bad-apple.dat`预处理文件，然后直接用它播放：
```
python charAnimePlayer.py bad-apple.dat -fps 50
```

播放预处理文件任可以指定帧率，但不可以设置宽高和播放声音了。