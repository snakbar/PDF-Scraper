# Gather Chip data sent to us from ALPAC

import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sys
from pathlib import Path
import os

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
print (root.filename)

# Filepath to the pdf you want to scrape (want to add something recursive in the future)
pdfpath = root.filename

# Open the dumb file

pdfFileObj = open(pdfpath, 'rb')

# Read the stupid thing

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#counts the number of pages
#print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
pagecontent = pageObj.extractText()



# manipulate the text string into something I can work with

U0Count = pagecontent.count('U0')
JACount = pagecontent.count('JA')
if U0Count > JACount:
    tm9prefix = 'U0'
else:
    tm9prefix = 'JA'

TM9code = pagecontent.find(tm9prefix)

trimcont = len(pagecontent)-pagecontent.find("Weighted")
trimmedcontent = pagecontent[TM9code:-trimcont-49]
reportdate = pagecontent[TM9code+11:-(len(pagecontent)-(TM9code+19))]
frmtreportdate = reportdate.replace('/','-')
#print(frmtreportdate)
removelinbrk = trimmedcontent.replace('\n',';')

# split the block of text into individual loads

loads = removelinbrk.split(tm9prefix)

# Clean up the loads.  Get rid of extraneous information

cleanloads = ['blank']

for x in loads:
    tempload = x.split(';')
    if len(tempload) == 16:
        del tempload[2:6]
    else:
        del tempload[2:5]
    cleanloads.append(tempload)
    #print(tempload)
    tempload.clear

# Print to console

#for x in cleanloads:
    #print(x)

# print to File

outputfilepath = Path("C:/tester pdfs/chipreport " + frmtreportdate + ".txt")
print(outputfilepath)
outfile = open(outputfilepath, 'w')
original_out = sys.stdout
sys.stdout = outfile
for x in cleanloads:
    print(x)
sys.stdout = original_out

