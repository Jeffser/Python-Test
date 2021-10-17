import os, sys
from tkinter import *
import tkinter.ttk as ttk
from pytube import YouTube, Playlist
import urllib
from PIL import Image, ImageTk
from io import BytesIO
win = Tk()
win.title("LunaDownloader")
win.geometry("360x800")
#win.resizable(False, False)
link = "https://www.youtube.com/watch?v=cNoy_b_JYU0" #win.clipboard_get()
YT = YouTube(link)
cTitulo = Canvas(win, bg="lightblue", highlightthickness=0)
cTitulo.pack(fill="x")
lblTitulo = Label(cTitulo, text="Luna Downloader", font="Arial, 24", bg="lightblue").pack(anchor="center")

cLink = Canvas(win, bg="seagreen1", highlightthickness=0)
cLink.pack(fill="x")
lblLink = Label(cLink, text=YT.title, font="Arial, 12", bg="seagreen1").grid()

cBotones = Canvas(win, bg="snow", highlightthickness=0)
cBotones.pack(fill="x")
pngPlus = Image.open(BytesIO(urllib.request.urlopen("https://raw.githubusercontent.com/Tentrillicom/Python-Test/main/Data/add.png").read()))
pngPlus = pngPlus.resize((30, 30), Image.ANTIALIAS)
pngPlus = ImageTk.PhotoImage(pngPlus)
btnBotones = Button(cBotones, highlightthickness=0, image=pngPlus, bg="DarkOliveGreen1", bd = 0)
btnBotones.pack(fill="x", anchor="center", side=TOP)

pngDown = Image.open(BytesIO(urllib.request.urlopen("https://raw.githubusercontent.com/Tentrillicom/Python-Test/main/Data/download.png").read()))
pngDown = pngDown.resize((30, 30), Image.ANTIALIAS)
pngDown = ImageTk.PhotoImage(pngDown)
btn2Botones = Button(cBotones, highlightthickness=0, image=pngDown, bg="RoyalBlue1", bd = 0)
btn2Botones.pack(fill="x", anchor="center", side=TOP)

fVideos = Frame(win)
fVideos.pack(expand=True, fill=BOTH)
cVideos = Canvas(fVideos, bg="LemonChiffon2", scrollregion=(0,0,500,500))
vbVideos = Scrollbar(fVideos, orient=VERTICAL, troughcolor="LemonChiffon2")
vbVideos.pack(side=RIGHT, fill=Y)
vbVideos.config(command=cVideos.yview)
cVideos.config(yscrollcommand=vbVideos.set)
cVideos.pack(fill=BOTH, expand=True)

cCreditos = Canvas(win, bg="grey20", highlightthickness=0)
cCreditos.pack(fill="x")
lblCreditos = Label(cCreditos, text="Jeffry Samuel Eduarte Rojas | Tentri#5008", font="Arial, 12", fg="snow", bg="grey20").pack(anchor="center")
win.mainloop()
