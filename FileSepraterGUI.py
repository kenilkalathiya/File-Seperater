import tkinter as tk
from tkinter import Image, ttk
import tkinter.messagebox as msg
from PIL import Image, ImageTk
import os, shutil
from tkinter import filedialog
import subprocess


# tkinter main windows initilizing
win = tk.Tk()
win.title('File Seperater')
win.geometry('500x250')
win.grid_rowconfigure(0, weight=0)
win.grid_columnconfigure(0, weight=0)


# background image 
img = ImageTk.PhotoImage(Image.open("./bg.png").resize((800, 550), Image.ANTIALIAS))
imgLabel = tk.Label(win, image=img)
imgLabel.img = img  
imgLabel.place(relx=0.5, rely=0.5, anchor='center')


# Logic Function
def browseFunc():
    pathEntryVar = filedialog.askdirectory()
    pathEntry.insert(0, pathEntryVar)


def seprationLoader(f_path, f_extension):
    return [file for file in os.listdir(f_path) for extension in f_extension if file.endswith(extension)]


def seprateFunc():
    folderPath = pathEntryVar.get()
    dictExtension = {
        'Audio_extension' : ('.mp3', '.mp4', '.wav','flac'),
        'Video_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
        'Documents_extension' : ('.doc','.docx','.pdf','.txt','.pptx'),
    }

    for extType, extTuple in dictExtension.items():
        fname = extType.split('_')[0] + '_Files'
        fpath = os.path.join(folderPath, fname)
        if os.path.exists(fpath):
            break
        else:
            os.mkdir(fpath)
        for item in seprationLoader(folderPath, extTuple):
            itemPath = os.path.join(folderPath,item)
            itemNewPath = os.path.join(fpath,item)
            shutil.move(itemPath,itemNewPath)
    msg.showinfo("Seperated","Your file has been seprated!")

def openFolderFuc():
    subprocess.Popen(f"explorer /select,{os.path.normpath(pathEntryVar.get())}")




# Labels
pathLabel = ttk.Label(win, text='File Path')
pathLabel.grid(row=0,column=0, padx=10, pady=30)
pathLabel.configure(font=1)

# Entry Boxes
pathEntryVar = tk.StringVar()
pathEntry = ttk.Entry(win, width=25, textvariable=pathEntryVar)
pathEntry.grid(row=0,column=1)

# Buttons
browseBtn = ttk.Button(win,text='Browse', style="TButton",  command = browseFunc)
browseBtn.grid(row=0,column=2, padx= 20)

openBtn = ttk.Button(win,text='Open', style="TButton",  command = openFolderFuc)
openBtn.grid(row=1,column=2, padx= 20)

seprateBtn = ttk.Button(win,text='Seperate', command=seprateFunc)
seprateBtn.grid(row=1,column=0, columnspan=2)

win.mainloop()
