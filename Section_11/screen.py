import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

# This id for the title
label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# General grid formatting
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# For the file list
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/home/darby/Documents/udemyProjects/udemyPython'):
    fileList.insert(tkinter.END, zone)

# For the file list's scroll bar
listScroll = tkinter.Scrollbar(mainWindow, orient="vertical", command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# For the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)
# Radio Buttons
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Display/field that shows the result
resultLablel = tkinter.Label(mainWindow, text='Result')
resultLablel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# For the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# Date labels
dayLable = tkinter.Label(dateFrame, text='Day')
monthLable = tkinter.Label(dateFrame, text='Month')
yearLable = tkinter.Label(dateFrame, text='Year')
dayLable.grid(row=0, column=0, sticky='w')
monthLable.grid(row=0, column=1, sticky='w')
yearLable.grid(row=0, column=2, sticky='w')
# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=1900, to=2100)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# ok/cancel buttons
okButton = tkinter.Button(mainWindow, text='Ok')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()
print(rbValue.get())