# Whisper GUI

本工具是python tkinter编写的一个简单的Gui，任务批量管理器。通过Gui选项生成*CMD*(command),来调用whisper，达到批量生成，管理的目的。



## 注意：

![image-20230213182634259](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230213182634259.png)

关于拓展选项 有朋友反应说这个"禁用"开启后，会出现断句不精准的问题，会比较机械的按照时间断句，而不是一整句话断开一次。

About the expansion option Some people say that when this "disable" option is turned on, there will be a problem of imprecise sentence break, which will be more mechanical according to the time break, instead of a whole sentence break once.

但是有时候关闭这个选项，个别情况会重复一句话。这种情况也和原视频时间戳错误有关。官方好像也没有很好的解决这个问题。

However, sometimes when this option is turned off, a sentence will be repeated in some cases. This situation is also related to the original video timestamp error. Officials do not seem to have a good solution to this problem.

具体开不开就大家视情况而定吧。我这边先默认关闭了，按官方原生的配置来。

The specific open or not on the situation depends on it. My side first closed by default, according to the official native configuration.

## 功能

支持的操作如下

1. 支持文件/文件夹拖入，或批量选择加载任务
2. 显示每个任务的状态
3. 可以对每一个文件任务单独设置不同的配置
4. Gui界面支持自定义大小调整，自适应界面
5. 对官方指令进行一定的修改，优化。改善长音频，语句重复的问题，识别错误的。
6. 软件自带功能将视频转化为aac音频，并且转化过程中重建时间戳，提高转化成功率
7. 可以选择指定的设备(CPU、显卡)
8. 支持将生成的srt字幕文件，复制到同目录下，并编辑为相同的文件名
9. 在支持whisper的前提下，增加支持whisperx，这个项目有更多的选项和拓展功能，详细请看相关目录。
10. 支持任务完成时间统计

## 界面

![image-20230205164851836](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205164851836.png)

![image-20230205170946355](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205170946355.png)

还有英文版的界面

![image-20230205172938535](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205172938535.png)

![image-20230205171031737](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205171031737.png)

## 安装

需要自行安装Python 3，cuda，whisper以及FFmpeg。

本工具是按照有显卡的版本设计的，纯cpu环境暂无测试，可能需要修改一下代码。

本工具只是提供方便操作的Gui界面，适合有一定基础的人使用。



### 请确认已有Pyhton以及FFmpeg

```
python --version
ffmpeg -version
```

### 执行run.vbs/run.bat

这样启动可以无窗口直接启动

### 双击执行Whisper_Gui.py/Whisper_Gui_en.py

有黑窗，但可以看到程序运行和输出

## 致谢

部分灵感来源于https://github.com/ADT109119/WhisperGUI

whisperx：https://github.com/m-bain/whisperX
