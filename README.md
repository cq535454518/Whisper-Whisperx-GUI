# Whisper GUI


本工具是python tkinter编写的一个简单的Gui，任务批量管理器。通过Gui选项生成*CMD*(command),来调用whisper，达到批量生成，管理的目的。

This tool is a simple Gui, task batch manager, written by python tkinder. Use the Gui option to generate * CMD * (command) to call Whisper to achieve the purpose of batch generation and management.



## 功能Function



支持的操作如下
The supported operations are as follows



1. 支持文件/文件夹拖入，或批量选择加载任务
1. Support file/folder dragging or batch selection of loading tasks

2. 显示每个任务的状态
2. Display the status of each task

3. 可以对每一个文件任务单独设置不同的配置
3. You can set different configurations for each file task

4. Gui界面支持自定义大小调整，自适应界面
4. Gui interface supports customized resizing and adaptive interface

5. 对官方指令进行一定的修改，优化。改善长音频，语句重复的问题，识别错误的。
5. Modify and optimize the official instructions. Improve the problem of long audio and repeated statements, and identify the wrong ones.

6. 软件自带功能将视频转化为aac音频，并且转化过程中重建时间戳，提高转化成功率
6. The software has its own function to convert video into aac audio, and reconstruct the timestamp during the conversion process to improve the conversion success rate

7. 可以选择指定的设备(CPU、显卡)
7. You can select the specified device (CPU, graphics card)

8. 支持将生成的srt字幕文件，复制到同目录下，并编辑为相同的文件名
8. Support to copy the generated srt subtitle file to the same directory and edit it to the same file name

9. 在支持whisper的前提下，增加支持whisperx，这个项目有更多的选项和拓展功能，详细请看相关目录。
9. On the premise of supporting Whisper, add support for Whisperx. This project has more options and expanded functions. Please refer to the relevant directory for details.

10. 支持任务完成时间统计

10. Support task completion time statistics

## 界面Interface

![image-20230205164851836](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205164851836.png)

![image-20230205170946355](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205170946355.png)

还有英文版的界面
There is also an English version of the interface

![image-20230205172938535](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205172938535.png)

![image-20230205171031737](https://cdn.jsdelivr.net/gh/cq535454518/cq_images@main/img1/image-20230205171031737.png)

## 安装install

需要自行安装Python 3，cuda，whisper以及FFmpeg。
You need to install Python 3, cuda, Whisper and FFmpeg by yourself.
本工具是按照有显卡的版本设计的，纯cpu环境暂无测试，可能需要修改一下代码。
This tool is designed according to the version with graphics card. There is no test in the pure cpu environment, and the code may need to be modified.
本工具只是提供方便操作的Gui界面，适合有一定基础的人使用。
This tool only provides a user-friendly gui interface, which is suitable for people with a certain foundation.
