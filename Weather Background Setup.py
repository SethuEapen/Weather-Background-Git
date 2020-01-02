from tkinter import *
from tkinter import filedialog
import os

setup = "C:/Program Files/Weather Background Changer/setup.txt"
file = open(setup, 'r')
f = file.readlines()
newList = []
for line in f:
    newList.append(line[:-1])
path = newList[0]
textSize = newList[1]
city = newList[2]
api_key = newList[3]
file.close()

#set up window
root = Tk()
root.title("Weather Background Setup")
root.resizable(False, False)
root.iconbitmap('WeatherBackground.ico')

#create file explorer
fileFrame = Frame(root)
fileFrame.pack()

fileLabel = Label(fileFrame, text=path)
fileLabel.pack(side=LEFT)

def setDir():
    fileLabel['text'] = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    

fileButton = Button(fileFrame, text="Browse...", command=setDir)
fileButton.pack(side=RIGHT)

#setAPIKEY
APIFrame = Frame(root)
APIFrame.pack()

APILabel = Label(APIFrame, text=api_key)
APILabel.pack(side=RIGHT)

APIText = StringVar()
APITB = Entry(APIFrame, textvariable=APIText, bg='light gray')
APIText.set(api_key)
APITB.pack(side=LEFT)

#set city
cityFrame = Frame(root)
cityFrame.pack()

cityLabel = Label(cityFrame, text=city)
cityLabel.pack(side=RIGHT)

cityText = StringVar()
cityTB = Entry(cityFrame, textvariable=cityText, bg='light gray')
cityText.set(city)
cityTB.pack(side=LEFT)

#set Text size
sizeFrame = Frame(root)
sizeFrame.pack()

OptionList = [] 

for i in range(100):
    OptionList.append(i)

variable = StringVar(root)
variable.set(textSize)
opt = OptionMenu(sizeFrame, variable, *OptionList)
opt.pack(side=LEFT)

optionLabel = Label(sizeFrame, text=textSize)
optionLabel.pack(side=RIGHT)

#setVariables
def set():
    filew = open(setup, 'w')
    path = fileLabel['text']
    textSize = variable.get()
    optionLabel['text'] = variable.get()
    cityLabel['text'] = cityTB.get()
    APILabel['text'] = APITB.get()
    filew.write(path + '\n')
    filew.write(textSize + '\n')
    filew.write(cityTB.get() + '\n')
    filew.write(APITB.get() + '\n')
    filew.close()

def test():
    set()
    os.chdir('/Program Files/Weather Background Changer/')
    os.system('python Weather2Final.pyw')

setters = Frame(root)
setters.pack()
fileButton = Button(setters, text="Set", command=set)
fileButton.pack(side=RIGHT)
fileButton = Button(setters, text="Test", command=test)
fileButton.pack(side=LEFT)

root.mainloop()

