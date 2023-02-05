from tkinter import *
from tkinter.ttk import *
import windnd
import tkinter.filedialog
import os
import tkinter as tk
import torch
from tkinter import messagebox
import subprocess
import re
import threading
import time
import shutil

devices = ['cpu']
object_list = []
config_data = {}


"""
全局通用函数
"""


def minute_operation(start_time, end_time):
    sum_stamp = end_time - start_time
    # print("总的时间戳是{}".format(sum_stamp))
    end_tuble = time.localtime(sum_stamp)
    # print("总时间戳的时间元组{}".format(end_tuble))
    # 因为由时间戳变成的时间元组，所以起始时间为8点开始，所以我们减去8，这样起始时间就是0点开始
    sum_time = f"{end_tuble.tm_hour - 8}:{time.strftime('%M:%S', (end_tuble))}"
    print("Time difference is{}".format(sum_time))
    return sum_time


# 自动隐藏滚动条
def scrollbar_autohide(bar, widget):
    def show():
        bar.lift(widget)

    def hide():
        bar.lower(widget)

    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_table_task_list = self.__tk_table_task_list()
        self.tk_tabs_xuanxiang_ka = Frame_xuanxiang_ka(self)
        self.tk_button_processButton = self.__tk_button_processButton()
        self.tk_input_output_dir = self.__tk_input_output_dir()
        self.tk_radio_button_translateToEnglish = self.__tk_radio_button_translateToEnglish()
        self.tk_label_label2 = self.__tk_label_label2()
        self.tk_radio_button_translateToSrt = self.__tk_radio_button_translateToSrt()
        self.tk_button_selectPhotoPathButton = self.__tk_button_selectSubPathButton()
        self.tk_button_delete_all = self.__tk_button_delete_all()
        self.tk_button_delete_one = self.__tk_button_delete_one()
        self.tk_button_selectPhotoFileButton = self.__tk_button_selectPhotoFileButton()
        self.tk_label_rwm_yulan = self.__tk_label_rwm_yulan()
        self.tk_input_renwu_text = self.__tk_input_renwu_text()
        self.tk_radio_button_run_whisper_fun = self.__tk_radio_button_run_whisper_fun()
        self.tk_radio_button_video_to_audio = self.__tk_radio_button_video_to_audio()
        self.tk_button_Reset_one = self.__tk_button_Reset_one()
        self.tk_button_application_config = self.__tk_button_application_config()

    def create_all_config(self, obj_list):
        config = {}
        for obj in obj_list:
            obj_type = type(obj).__name__
            if obj_type == "Combobox":
                config[obj.name] = obj.get()
                if obj.name == "device":
                    config[obj.name] = self.tk_tabs_xuanxiang_ka.tk_tabs_xuanxiang_ka_0.deviceDecode()
            elif obj_type in ["Radiobutton", "Checkbutton"]:
                config[obj.name] = obj.var.get()
        return config



    def __win(self):
        self.title("whisper Gui")
        # 设置窗口大小、居中
        width = 620
        height = 620
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        # self.resizable(width=False, height=False)

    def __tk_table_task_list(self):
        self.num = 0

        # 定义添加文件到 Treeview 的函数
        def add_files_to_list(file_paths):
            global config_data
            for n, rootdir in enumerate(file_paths):
                if os.path.isdir(rootdir):
                    # print("这是一个文件夹\n")
                    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
                        for filename in filenames:  # 文件名
                            tk_table.insert('', 'end', values=[self.num, os.path.join(parent, filename), "Waiting"])
                            file_config = self.create_all_config(object_list)
                            config_data[self.num] = {}
                            config_data[self.num]['path'] = os.path.join(parent, filename)
                            config_data[self.num]['config'] = file_config
                            self.num += 1

                elif os.path.isfile(rootdir):
                    # print("这是一个文件\n")
                    tk_table.insert('', 'end', values=[self.num, rootdir, "Waiting"])
                    file_config = self.create_all_config(object_list)
                    config_data[self.num] = {}
                    config_data[self.num]['path'] = rootdir
                    config_data[self.num]['config'] = file_config
                    self.num += 1

                else:
                    print(rootdir + " Is not a file or folder\n")
                    print("\r\n" + rootdir + " The path cannot be found or the length of the path/file name is too long. Please reduce the file length")
            tk_table.yview('moveto', 1)

        # 表头字段 表头宽度
        columns = {"ID": 69, "Task": 419, "Status": 69}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width)  # stretch 不自动拉伸

        tk_table.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.35)
        windnd.hook_dropfiles(self, func=add_files_to_list,
                              force_unicode=True)  # 可改为init_data_Text限定拖入范围,force_unicode代表启用un编码

        return tk_table

    def __tk_button_delete_all(self):
        def all_delete():
            global config_data
            self.tk_table_task_list.delete(*self.tk_table_task_list.get_children())
            self.num = 0
            config_data = {}


        btn = Button(self, text="Clear All", command=all_delete)
        btn.place(relx=0.03, rely=0.4, relwidth=0.16, height=26)
        return btn

    def __tk_button_delete_one(self):
        def one_delete():
            i = self.tk_table_task_list.selection()
            if i:
                print(self.tk_table_task_list.item(i[0], "values")[1], "--Deleted successfully")
                self.tk_table_task_list.delete(i[0])

        btn = Button(self, text="Delete", command=one_delete)
        btn.place(relx=0.225, rely=0.4, relwidth=0.16, height=26)
        return btn

    def __tk_button_selectPhotoFileButton(self):
        # 定义选择文件的回调函数
        def select_files():
            global config_data
            # 让用户选择多个文件
            files = tkinter.filedialog.askopenfilenames()
            # 遍历文件列表，向 Listbox 中添加文件名
            for paths in files:
                self.tk_table_task_list.insert('', 'end', values=[self.num, paths, "Waiting"])
                file_config = self.create_all_config(object_list)
                config_data[self.num] = {}
                config_data[self.num]['path'] = paths
                config_data[self.num]['config'] = file_config
                self.num += 1

        btn = Button(self, text="Select Files", command=select_files)
        btn.place(relx=0.42, rely=0.4, relwidth=0.16, height=26)
        return btn

    def __tk_button_Reset_one(self):
        def one_Reset():
            i = self.tk_table_task_list.selection()
            if i:
                print(self.tk_table_task_list.item(i[0], "values")[1], "--Reset task successfully")
                self.tk_table_task_list.set(i[0], column='Status', value="Waiting")

        btn = Button(self, text="Reset Task", command=one_Reset)
        btn.place(relx=0.615, rely=0.4, relwidth=0.16, height=26)
        return btn

    def __tk_button_application_config(self):
        def application_config():
            global config_data
            file_config = self.create_all_config(object_list)
            for n in range(len(config_data)):
                config_data[n]['config'] = file_config

        btn = Button(self, text="Configure to all", command=application_config)
        btn.place(relx=0.81, rely=0.4, relwidth=0.16, height=26)
        return btn

    def __tk_button_processButton(self):
        def create_commandStr(file_path, output_dirInput, tree_num):
            now_id = self.tk_table_task_list.item(tree_num, "values")[0]
            task_config = config_data[int(now_id)]['config']

            # 判断whisper还是whisperx
            if task_config["main_program"] == '1':
                commandStr = "whisperx "
            else:
                commandStr = "whisper "

            commandStr = commandStr + '"%s"' % file_path
            languageInput = task_config["language"]
            if languageInput != "auto_detect":
                commandStr = commandStr + " --language %s " % languageInput
            deviceInput = task_config["device"]
            commandStr = commandStr + " --device %s " % deviceInput
            commandStr = commandStr + " --model %s " % task_config["model"]

            if output_dirInput != "":
                commandStr = commandStr + " --output_dir %s " % output_dirInput
            # commandStr = commandStr + " --model_dir %s " % ("model")
            if task_config["translate"] == '1':
                commandStr = commandStr + " --task %s " % ("translate")
            # print(os.system("echo %s"%commandStr))

            # 针对拓展选项的判断
            # 禁用--condition_on_previous_text 设置为False（减少幻觉）
            if task_config["disable_condition"] == '1':
                commandStr = commandStr + " --condition_on_previous_text %s " % ("False")

            # 启用vad_filter(whisperx)
            if task_config["enable_vad_filter"] == '1' and self.run_whisper_fun.get() == '1':
                commandStr = commandStr + " --vad_filter"

            return commandStr

        def run_command(file_path, tree_num):
            # 检测任务是否已经完成过
            if self.tk_table_task_list.item(tree_num, "values")[2] != "Waiting":
                print("This task has already been processed")
                return 0

            now_id = self.tk_table_task_list.item(tree_num, "values")[0]
            task_config = config_data[int(now_id)]['config']
            video_check = re.search(r'(.3gp|.asf|.avi|.dat|.flv|.m4v|.mkv|.mov|.mp4|.mpeg|.mpg|.ogg|.ogv|.rm|.ts|.vob|.webm|.wmv|.m2ts)$', file_path, re.M | re.I)
            audio_check = re.search(r'(.aac|.aiff|.alac|.amr|.ape|.au|.flac|.m4a|.m4p|.mid|.mp3|.ogg|.ra|.wav|.wma)$', file_path, re.M | re.I)
            if not (video_check or audio_check):
                self.tk_table_task_list.set(tree_num, column='Status', value="Type Error")
                return 0
            File_old = ""
            output_dirInput = self.tk_input_output_dir.get()
            temp_path = os.path.join(os.getcwd() + "\\temp")
            # 如果转化开关打开，那么视频将会转化成音频后再处理
            if task_config["Fix Timestamp"] != "Disabled" and video_check:
                # 生成相关配置
                filename = os.path.basename(file_path)
                filename = re.sub(r'\.[^.]*$', '', filename)  # 去后缀名
                audio_path = os.path.join(temp_path, filename + ".aac")
                if not os.path.exists(temp_path):
                    os.makedirs(temp_path)
                self.tk_table_task_list.set(tree_num, column='Status', value="Converting~")
                if task_config["Fix Timestamp"] == "full Fix (Slow, but accurate)":
                    commandStr = f'ffmpeg -i "{file_path}" -c:v copy -c:a aac -af asetpts=PTS-STARTPTS -y "{audio_path}"'
                    print(commandStr)
                    result = subprocess.run(commandStr)
                    print("Command line return code:", result.returncode)
                else:
                    commandStr = f'ffmpeg -ss 0 -accurate_seek -i "{file_path}" -codec copy -avoid_negative_ts 1 -y "{audio_path}"'
                    print(commandStr)
                    out = subprocess.Popen(commandStr, creationflags=subprocess.CREATE_NO_WINDOW,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(out.communicate())

                if not os.path.exists(audio_path):
                    print(audio_path, "--Failed to generate audio!")
                else:
                    File_old = file_path
                    file_path = audio_path

            self.tk_table_task_list.set(tree_num, column='Status', value="Running~")
            commandStr = create_commandStr(file_path, output_dirInput, tree_num)
            print(commandStr)
            start_time = time.time()
            out = subprocess.run(commandStr)
            # (out, err) = out.communicate()
            end_time = time.time()


            if out.returncode == 0:
                time_text = minute_operation(start_time, end_time)
                result = str(time_text) + "Finish"
            else:
                result = "Error"

            self.tk_table_task_list.set(tree_num, column='Status', value=result)

            # 将srt移动到文件同目录下
            if task_config["Export srt"] == '1':
                filename = os.path.basename(file_path) + ".srt"

                # 生成新路径
                if File_old == "":
                    base_name, ext = os.path.splitext(file_path)
                else:
                    base_name, ext = os.path.splitext(File_old)

                new_file_path = base_name + ".srt"
                # 判断文件是否存在
                if not os.path.exists(os.path.join(output_dirInput, filename)):
                    self.tk_table_task_list.set(tree_num, column='Status', value="Error subtitles")
                    if os.path.exists(temp_path):
                        shutil.rmtree(temp_path)
                    return 0

                try:
                    # 判断文件是否存在
                    if os.path.exists(new_file_path):
                        # 存在，则删除文件
                        os.remove(new_file_path)
                    print(os.path.join(output_dirInput, filename))
                    print(new_file_path)
                    shutil.copy(os.path.join(output_dirInput, filename), new_file_path)
                    print("Move srt to the file directory successfully")
                    if os.path.exists(temp_path):
                        shutil.rmtree(temp_path)

                except BaseException as e:
                    self.tk_table_task_list.set(tree_num, column='Status', value="Mobile srt error")
                    print(e)

            # messagebox.showinfo(title="消息", message="处理完成")

        def __process():
            tree_list = self.tk_table_task_list.get_children()
            for tree_num in tree_list:
                now_id = self.tk_table_task_list.item(tree_num, "values")[0]
                file_path = config_data[int(now_id)]['path']
                run_command(file_path, tree_num)


        def process():
            T = threading.Thread(target=__process)
            T.start()

        btn = Button(self, text="Execution", command=process)
        btn.place(relx=0.64, rely=0.83, width=140, height=60)
        return btn

    def __tk_label_rwm_yulan(self):
        label = Label(self, text="Task Preview", anchor="center")
        label.place(relx=0.04, rely=0.46, width=100, height=24)
        return label

    def __tk_input_renwu_text(self):
        ipt = Entry(self)
        ipt.place(relx=0.22, rely=0.46, relwidth=0.67, height=24)
        return ipt

    def __tk_label_label2(self):
        label = Label(self, text="Subtitle output", anchor="center")
        label.place(relx=0.04, rely=0.52, width=100, height=24)
        return label

    def __tk_input_output_dir(self):
        ipt = Entry(self)
        ipt.place(relx=0.22, rely=0.52, relwidth=0.67, height=24)
        ipt.insert(0, os.getcwd() + "\\output")
        return ipt

    def __tk_button_selectSubPathButton(self):
        def selectPhotoFolder():
            folder_PATH = tkinter.filedialog.askdirectory()
            self.tk_input_output_dir.delete(0, 'end')
            self.tk_input_output_dir.insert(0, folder_PATH)

        btn = Button(self, text="...", command=selectPhotoFolder)
        btn.place(relx=0.91, rely=0.52, width=40, height=26)
        return btn

    def __tk_radio_button_translateToEnglish(self):
        self.translateToEnglishVar = StringVar(self, value="0")
        translateToEnglish = Checkbutton(self, text="Whether to translate into English", variable=self.translateToEnglishVar, onvalue="1",
                                         offvalue="0")
        translateToEnglish.place(relx=0.60, rely=0.67, width=238, height=24)
        object_list.append(translateToEnglish)
        translateToEnglish.name = "translate"
        translateToEnglish.var = self.translateToEnglishVar
        return translateToEnglish

    def __tk_radio_button_translateToSrt(self):
        self.translateToSrtVar = StringVar(self, value="1")
        translateToSrt = Checkbutton(self, text="Whether copy srt files to directory", variable=self.translateToSrtVar, onvalue="1",
                                     offvalue="0")
        translateToSrt.place(relx=0.60, rely=0.72, width=238, height=24)
        object_list.append(translateToSrt)
        translateToSrt.name = "Export srt"
        translateToSrt.var = self.translateToSrtVar
        return translateToSrt

    def __tk_radio_button_video_to_audio(self):
        label = Label(self, text="Fix video timestamp", anchor="center")
        label.place(relx=0.42, rely=0.62, width=240, height=24)
        cb = Combobox(self, state="readonly")
        cb['value'] = ("Disabled", "Quick Fix", "full Fix (Slow, but accurate)")
        cb.current(2)
        cb.place(relx=0.71, rely=0.62, width=160, height=24)
        # 存储config相关
        object_list.append(cb)
        cb.name = "Fix Timestamp"
        return cb

    def __tk_radio_button_run_whisper_fun(self):
        self.run_whisper_fun = StringVar(self, value="0")
        radiobutton1 = Radiobutton(self, text="whisper", variable=self.run_whisper_fun, value=0)
        radiobutton1.place(relx=0.58, rely=0.77, width=80, height=24)
        radiobutton2 = Radiobutton(self, text="whisperx", variable=self.run_whisper_fun, value=1)
        radiobutton2.place(relx=0.80, rely=0.77, width=80, height=24)
        # 存储config相关
        # radiobutton1.bind("<Button-1>", update_data)
        # radiobutton2.bind("<Button-1>", update_data)
        radiobutton1.var = self.run_whisper_fun
        radiobutton2.var = self.run_whisper_fun
        object_list.append(radiobutton1)
        object_list.append(radiobutton2)
        radiobutton1.name = "main_program"
        radiobutton2.name = "main_program"
        return 1


class Frame_xuanxiang_ka(Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):

        self.tk_tabs_xuanxiang_ka_0 = Frame_xuanxiang_ka_0(self)
        self.add(self.tk_tabs_xuanxiang_ka_0, text="General")

        self.tk_tabs_xuanxiang_ka_1 = Frame_xuanxiang_ka_1(self)
        self.add(self.tk_tabs_xuanxiang_ka_1, text="Expanded")

        self.place(relx=0.06, rely=0.58, width=274, height=220)

class Frame_xuanxiang_ka_0(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_label_usingModel = self.__tk_label_label_usingModel()
        self.tk_label_label_usingDevice = self.__tk_label_label_usingDevice()
        self.tk_label_box_usingDevice = self.__tk_label_label_language()
        self.tk_select_box_usingModel = self.__tk_select_box_usingModel()
        self.tk_select_box_usingDevice = self.__tk_select_box_usingDevice()
        self.tk_select_box_usingLanguage = self.__tk_select_box_usingLanguage()
        self.detectAvailableDevice()

    def __frame(self):
        self.place(x=20, y=290, width=298, height=229)

    def __tk_label_label_usingModel(self):
        label = Label(self, text="model", anchor="center")
        label.place(x=20, y=30, width=56, height=24)
        return label

    def __tk_select_box_usingModel(self):
        cb = Combobox(self, state="readonly")
        cb['value'] = ("tiny.en", "tiny", "base.en", "base", "small.en", "small", "medium.en", "medium", "large-v1",
                       "large-v2", "large")
        # cb['value'] = ('tiny', 'base', 'small', 'medium', 'large')

        cb.current(7)
        cb.place(x=90, y=30, width=160, height=24)
        object_list.append(cb)
        cb.name = "model"
        return cb

    def __tk_label_label_usingDevice(self):
        label = Label(self, text="device", anchor="center")
        label.place(x=20, y=90, width=56, height=24)
        return label

    def deviceDecode(self):
        dev = devices.index(self.deviceVar.get())
        if dev > 0:
            return ("cuda:%s" % (dev - 1))
        else:
            return ("cpu")

    def detectAvailableDevice(self):
        if torch.cuda.is_available():
            for i in range(torch.cuda.device_count()):
                devices.append(torch.cuda.get_device_name(i))
            # print(torch.cuda.device_count())
            if torch.cuda.device_count() > 0:
                self.tk_select_box_usingDevice['value'] = devices
                self.tk_select_box_usingDevice.current(1)
        return

    def __tk_select_box_usingDevice(self):
        def deviceChange(index, value, op):
            # print("%s %s %s"%(index, value, op))
            dev = devices.index(cb.get())
            if dev > 0:
                print("Select the device as: cuda:%s" % (dev - 1))
            else:
                print("Select the device as: cpu")

        self.deviceVar = tk.StringVar()
        self.deviceVar.trace("w", deviceChange)
        cb = Combobox(self, state="readonly", textvariable=self.deviceVar)
        cb['value'] = devices
        cb.current(0)
        cb.place(x=90, y=90, width=160, height=24)
        object_list.append(cb)
        cb.name = "device"
        return cb

    def __tk_label_label_language(self):
        label = Label(self, text="language", anchor="center")
        label.place(x=20, y=150, width=56, height=24)
        return label

    def __tk_select_box_usingLanguage(self):
        cb = Combobox(self, state="readonly")
        languages = ["auto_detect", "Chinese", "English", "Japanese", "Afrikaans", "Albanian", "Amharic", "Arabic",
                     "Armenian", "Assamese", "Azerbaijani", "Bashkir",
                     "Basque", "Belarusian", "Bengali", "Bosnian", "Breton", "Bulgarian", "Burmese", "Castilian",
                     "Catalan",
                     "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Faroese", "Finnish",
                     "Flemish",
                     "French", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian", "Haitian Creole",
                     "Hausa",
                     "Hawaiian", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Italian", "Japanese",
                     "Javanese",
                     "Kannada", "Kazakh", "Khmer", "Korean", "Lao", "Latin", "Latvian", "Letzeburgesch", "Lingala",
                     "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori",
                     "Marathi", "Moldavian", "Moldovan", "Mongolian", "Myanmar", "Nepali", "Norwegian", "Nynorsk",
                     "Occitan",
                     "Panjabi", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Pushto", "Romanian", "Russian",
                     "Sanskrit", "Serbian", "Shona", "Sindhi", "Sinhala", "Sinhalese", "Slovak", "Slovenian", "Somali",
                     "Spanish", "Sundanese", "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Tatar", "Telugu",
                     "Thai",
                     "Tibetan", "Turkish", "Turkmen", "Ukrainian", "Urdu", "Uzbek", "Valencian", "Vietnamese", "Welsh",
                     "Yiddish", "Yoruba"]
        cb['values'] = languages
        cb.current(0)
        cb.place(x=90, y=150, width=160, height=24)
        object_list.append(cb)
        cb.name = "language"
        return cb

class Frame_xuanxiang_ka_1(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_check_button_jy_condition_on = self.__tk_check_button_jy_condition_on()
        self.tk_check_button_qy_vad_filter = self.__tk_check_button_qy_vad_filter()
        self.tk_label_vad_filter_say = self.__tk_label_vad_filter_say()
    def __frame(self):
        self.place(x=20, y=290, width=298, height=229)


    def __tk_check_button_jy_condition_on(self):
        self.jy_condition_on = StringVar(self, value="1")
        cb = Checkbutton(self,text="Disable--condition_on_pr.. Reduce errors", variable=self.jy_condition_on, onvalue="1",
                                     offvalue="0")
        cb.place(x=10, y=30, width=280, height=49)
        object_list.append(cb)
        cb.name = "disable_condition"
        cb.var = self.jy_condition_on
        return cb

    def __tk_check_button_qy_vad_filter(self):
        self.qy_vad_filter = StringVar(self, value="0")
        cb = Checkbutton(self,text="Enable -- vad_Filter(Whisperx only)", variable=self.qy_vad_filter, onvalue="1",
                                     offvalue="0")
        cb.place(x=10, y=100, width=281, height=24)
        object_list.append(cb)
        cb.name = "enable_vad_filter"
        cb.var = self.qy_vad_filter
        return cb

    def __tk_label_vad_filter_say(self):
        label = Label(self,text="Add -- vad_ Filter flag to improve the \naccuracy and stability of time stamps", anchor="center")
        label.place(x=0, y=140, width=279, height=36)
        return label


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.reading_config = False
        self.__event_bind()

    def load_config_ui(self, evt):
        global config_data
        self.reading_config = True
        self.tk_input_renwu_text.delete(0, tk.END)
        if self.tk_table_task_list.selection():
            now_task_value = self.tk_table_task_list.item(self.tk_table_task_list.selection()[0], "values")
            now_name = os.path.basename(now_task_value[1])
            # print("当前选择：", now_name)
            self.tk_input_renwu_text.insert(0, now_name)
            # print("ID:", now_task_value[0])
            now_config = config_data[int(now_task_value[0])]['config']
            # print(now_config)
            for obj in object_list:
                obj_type = type(obj).__name__
                if obj_type == 'Combobox':
                    if obj.name == "device":
                        if "cuda:" in now_config.get(obj.name, ''):
                            name = torch.cuda.get_device_name(int(now_config.get(obj.name, '').replace("cuda:", "")))
                        else:
                            name = "cpu"
                        obj.set(name)
                    else:
                        obj.set(now_config.get(obj.name, ''))
                elif obj_type in ['Radiobutton', 'Checkbutton']:
                    obj.var.set(now_config.get(obj.name, 0))
        self.reading_config = False

    def keep_config(self, *args):
        global config_data
        if self.reading_config:
            return
        if self.tk_table_task_list.selection():
            now_task_value = self.tk_table_task_list.item(self.tk_table_task_list.selection()[0], "values")
            now_id = now_task_value[0]
            file_config = self.create_all_config(object_list)
            config_data[int(now_id)]['config'] = file_config
            print("Save configuration to task in real time", now_id)

    def __event_bind(self):
        self.tk_table_task_list.bind('<<TreeviewSelect>>', self.load_config_ui)
        # 当一些object发生改变时，绑定对应事件
        for obj in object_list:
            obj_type = type(obj).__name__
            if obj_type == 'Combobox':
                obj.bind('<<ComboboxSelected>>', self.keep_config)
            elif obj_type in ['Radiobutton', 'Checkbutton']:
                # obj.bind("<Button-1>", self.keep_config)
                obj.var.trace("w", self.keep_config)


if __name__ == "__main__":
    win = Win()
    win.mainloop()
