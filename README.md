# 鸡你太美

# Run
```
python jinitaimei.py
```

![](demo.gif)

## 有关字符动画的制作
### 需要：
 - python3
 - opencv

### 原理
用opencv读取视频帧，压缩，灰化，构造灰度字符串，用字符串替换每个像素。

### 创作你的字符动画
首先clone该repo，导入文件
```python
import sys
sys.path.append('./')
from CharAnimeBuilder import *
from CharAnimePlayer import *
```

然后构造灰度字符串
```python
a =  "@@@@@@@@@*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?   
```

构造builder,传入视频
```python
builder = CharAnimeBuilder(a,'ikun.mp4') 
```

输入宽高,目标持久化文件路径
```python
builder.build(130,40,'./f.dat')
```

此时同目录下已经出现了`f.dat`文件，加载持久化文件,设置帧率(1-60),初始化播放器
```python
player = CharAnimePlayer('./f.dat',10)
```
最后播放
```python
player.play()
```

在linux下测试通过，windows可能有些地方要改改