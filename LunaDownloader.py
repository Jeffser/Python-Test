from tkinter import *
win = Tk()
win.title("LunaDownloader")
win.geometry("360x800")
win.resizable(False, False)
text = win.clipboard_get()
lbl = Label(win, text=text).grid()
win.mainloop()

