import tkinter as tk
from tkinter import ttk
import os, shutil

dict_extension = {
    'audio_extension' : ('.mp3', '.mp4', '.wav','flac'),
    'vedio_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'documents_extension' : ('.doc','.docx','.pdf','.txt','.pptx'),
}

win = tk.Tk()
win.title('File Seperater')
win.geometry('800x550')
# Example(root).grid(sticky="nsew")
win.grid_rowconfigure(0, weight=0)
win.grid_columnconfigure(0, weight=0)

path_name = ttk.Label(win, text='Enter your File path : ')
path_name.grid(row=2,column=0)

# entrybox
path_var = tk.StringVar()
path_entrybox = ttk.Entry(win, width=25, textvariable=path_var)
path_entrybox.grid(row=2,column=1)


def file_seprater(f_path, f_extension):
    return [file for file in os.listdir(f_path) for extension in f_extension if file.endswith(extension)]

# Submit
def action():
    folderpath = path_var.get()

    for extension_type, extension_tuple in dict_extension.items():
        f_name = extension_type.split('_')[0] + 'Files'
        f_path = os.path.join(folderpath, f_name)
        if os.path.exists(f_path):
            break
        else:
            os.mkdir(f_path)
        for item in file_seprater(folderpath, extension_tuple):
            item_path = os.path.join(folderpath,item)
            item_new_path = os.path.join(f_path,item)
            shutil.move(item_path,item_new_path)


submit_button = ttk.Button(win,text='Seperate', command=action)
submit_button.grid(row=3,columnspan=2, pady=20)

win.mainloop()

