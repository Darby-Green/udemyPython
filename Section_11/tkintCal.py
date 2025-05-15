import tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('200x300')
mainWindow['padx'] = mainWindowPadding


title = tkinter.Label(mainWindow, text="Calculator")
title.grid(row=0, column=0, columnspan=4)

textBox = tkinter.Entry(mainWindow)
textBox.grid(row=1, column=0, columnspan=4)

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=2, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text= key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

# button1 = tkinter.Button(mainWindow, text='1')
# button2 = tkinter.Button(mainWindow, text='2')
# button3 = tkinter.Button(mainWindow, text='3')
# button4 = tkinter.Button(mainWindow, text='4')
# button5 = tkinter.Button(mainWindow, text='5')
# button6 = tkinter.Button(mainWindow, text='6')
# button7 = tkinter.Button(mainWindow, text='7')
# button8 = tkinter.Button(mainWindow, text='8')
# button9 = tkinter.Button(mainWindow, text='9')
# button0 = tkinter.Button(mainWindow, text='0')
# clearButton = tkinter.Button(mainWindow, text='C')
# CEButton = tkinter.Button(mainWindow, text='CE')
# plusButton = tkinter.Button(mainWindow, text='+')
# minusButton = tkinter.Button(mainWindow, text='-')
# multiplyButton = tkinter.Button(mainWindow, text='*')
# divideButton = tkinter.Button(mainWindow, text='/')
# equalsButton = tkinter.Button(mainWindow, text='=')


# button1.grid(row=2, column=0)
# button2.grid(row=2, column=1)
# button3.grid(row=2, column=2)
# plusButton.grid(row=2, column=3)
# button4.grid(row=3, column=0)
# button5.grid(row=3, column=1)
# button6.grid(row=3, column=2)
# minusButton.grid(row=3, column=3)
# button7.grid(row=4, column=0)
# button8.grid(row=4, column=1)
# button9.grid(row=4, column=2)
# multiplyButton.grid(row=4, column=3)
# clearButton.grid(row=5, column=0)
# button0.grid(row=5, column=1)
# CEButton.grid(row=5, column=2)
# divideButton.grid(row=5, column=3)
# equalsButton.grid(row=6, column=3)

mainWindow.mainloop()