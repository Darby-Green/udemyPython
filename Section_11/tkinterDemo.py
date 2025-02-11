import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello there")
mainWindow.geometry('640x480')
mainWindow.mainloop()