from tkinter import *
from pytube import YouTube, Playlist
win = Tk()
win.title("LunaDownloader")
win.geometry("360x800")
win.resizable(False, False)
link = win.clipboard_get()
YT = YouTube(link)
lbl = Label(win, text = YT.title).grid()
win.mainloop()
