from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sys
import os
from pathlib import Path
import time

#Initialise some Variables, Get the Window ready to roll

window = Tk()
window.title('Eat the Rich')
window.geometry('900x600')
cinpath = 'Please Select A PDF ----------->'
coutpath = 'Please Select A Target Folder -->'

def findtargetpdf(): #This function uses the filedialog to get the filepath to the target pdf
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                                 filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    cinpath = window.filename
    cinlabel.config(text=cinpath)

def findtargetfolder(): #This selects the target directory
    window.filename = filedialog.askdirectory(initialdir="/", title="Select folder")
    coutpath = window.filename
    coutlabel.config(text=coutpath)

#Buttons and labels for the target pdfs
cinlabel = Label(text=cinpath,borderwidth=3,relief='groove')
cinbutt = Button(text='findtarget',command= findtargetpdf)
cinlabel.grid(column=0,row=0,padx=10,pady=10)
cinbutt.grid(column=1,row=0,padx=10,pady=10)

#Buttons and Labels for the target directory
coutlabel = Label(text=coutpath,borderwidth=3,relief='groove')
coutbutt = Button(text='pick folder',command=findtargetfolder)
coutlabel.grid(column=0,row=1,padx=10,pady=10)
coutbutt.grid(column=1,row=1,padx=10,pady=10)


window.mainloop()






