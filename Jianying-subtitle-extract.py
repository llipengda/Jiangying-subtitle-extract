import json
import tkinter as tk
from tkinter import filedialog
import os
import getpass


def content(text: str):
    parts = text.split("><")
    for part in parts:
        if ">" in part and "<" in part:
            return part.split(">")[1].split("<")[0]


def json_to_txt(json_file_name, txt_file_name):
    with open(json_file_name, 'r', encoding='utf-8') as file:
        jsons = json.load(file)
    with open(txt_file_name, 'w', encoding='utf-8') as file:
        for item in jsons['materials']['texts']:
            file.write('%s\n' % content(item['content']))


def select_folder():
    selected_folder = filedialog.askdirectory(initialdir=files['default'])
    select_path.set(selected_folder)
    files['file'] = selected_folder + '/draft_content.json'


def totxt():
    json_to_txt(files['file'], files['file']+'.txt')
    os.system('notepad '+files['file']+'.txt')


username = getpass.getuser()
default_path = 'C:/Users/' + username + \
    '/AppData/Local/JianyingPro/User Data/Projects/com.lveditor.draft'
files = {'file': "", 'default': default_path}
window = tk.Tk()
window.title('剪映字幕提取')
select_path = tk.StringVar()
select_path.set(default_path)
tk.Label(window, text="工程文件夹路径：", font=('黑体', 12)).grid(
    column=0, row=0, rowspan=3)
tk.Entry(window, textvariable=select_path, width=25, font=('黑体', 12)).grid(
    column=1, row=0, rowspan=3)
tk.Button(window, text="打开文件夹", command=select_folder, font=('黑体', 12, 'bold')).grid(
    row=1, column=5)
tk.Label(window, text="\n").grid(column=4, row=1)
tk.Button(window, text="确定", command=totxt, font=(
    '黑体', 18, 'bold')).grid(row=8, column=1)
window.mainloop()
