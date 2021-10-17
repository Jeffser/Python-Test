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
win.update()
wHeight = win.winfo_height()
wWidth = win.winfo_width()
print(wHeight)
print(wWidth)
print(wWidth)
link = "https://www.youtube.com/watch?v=cNoy_b_JYU0" #win.clipboard_get()
YT = YouTube(link)
Videos = []
lVideos = []

#Canvas de titulo
cTitulo = Canvas(win, bg="lightblue", highlightthickness=0)
cTitulo.pack(fill="x")
lblTitulo = Label(cTitulo, text="Luna Downloader", font="Arial, 20", bg="lightblue").pack(anchor="center")

#Canvas de link
cLink = Canvas(win, bg="seagreen1", highlightthickness=0)
cLink.pack(fill="x")
lblLink = Label(cLink, text=YT.title, font="Arial, 8", bg="seagreen1")
lblLink.grid(row=0, column=0, sticky="nsew")
pngReload = Image.open(BytesIO(urllib.request.urlopen("https://raw.githubusercontent.com/Tentrillicom/Python-Test/main/Data/reload.png").read()))
pngReload = pngReload.resize(((int) (pngReload.width * wHeight /10000), (int) (pngReload.height * wHeight /10000)), Image.ANTIALIAS)
pngReload = ImageTk.PhotoImage(pngReload)

def relLink():
    global YT, link, lblLink
    link = win.clipboard_get()
    YT = YouTube(link)
    lblLink.config(text=YT.title)

btnLink = Button(cLink, image=pngReload, highlightthickness=0, bd=0, command=relLink)
btnLink.grid(row=0, column=1, sticky="nsew")
cLink.grid_columnconfigure(0, weight=10, uniform="group1")
cLink.grid_columnconfigure(1, weight=1, uniform="group1")
cLink.grid_rowconfigure(0, weight=1)

#Canvas Botones
cBotones = Canvas(win, bg="snow", highlightthickness=0)
cBotones.pack(fill="x")
pngPlus = Image.open(BytesIO(urllib.request.urlopen("https://raw.githubusercontent.com/Tentrillicom/Python-Test/main/Data/add.png").read()))
pngPlus = pngPlus.resize(((int) (pngPlus.width * wHeight /10000), (int) (pngPlus.height * wHeight /10000)), Image.ANTIALIAS)
pngPlus = ImageTk.PhotoImage(pngPlus)

pngDown = Image.open(BytesIO(urllib.request.urlopen("https://raw.githubusercontent.com/Tentrillicom/Python-Test/main/Data/download.png").read()))
pngDown = pngDown.resize(((int) (pngDown.width * wHeight /10000), (int) (pngDown.height * wHeight /10000)), Image.ANTIALIAS)
pngDown = ImageTk.PhotoImage(pngDown)

#Canvas Videos Base
fVideos = Frame(win, bg="LemonChiffon2")
fVideos.pack(expand=True, fill=BOTH)
cVideos = Canvas(fVideos, bg="LemonChiffon2", width=300, height=300, scrollregion=(0,0,500,500), highlightthickness=0)
vbVideos = Scrollbar(fVideos, orient=VERTICAL)
vbVideos.pack(side=RIGHT, fill=Y)
vbVideos.config(command=cVideos.yview)
cVideos.config(width=300,height=300)
cVideos.config(yscrollcommand=vbVideos.set)
cVideos.pack(fill=BOTH, expand=True, side=LEFT)

def Agregar():
    global Videos, lVideos, YT
    pngTN = Image.open(BytesIO(urllib.request.urlopen(YT.thumbnail_url).read()))
    pngTN = pngTN.resize(((int) (pngTN.width * wHeight /5000), (int) (pngTN.height * wHeight /5000)), Image.ANTIALIAS)
    pngTN = ImageTk.PhotoImage(pngTN)
    lVideos.append([])
    lVideos[len(lVideos)-1].append(Canvas(cVideos, bg="LemonChiffon1", highlightthickness=0))
    lVideos[len(lVideos)-1].append(Label(lVideos[len(lVideos)-1][0], bg="LemonChiffon1", font="Arial, 8", text=YT.title))
    lVideos[len(lVideos)-1].append(Label(lVideos[len(lVideos)-1][0], image=pngTN, bg="LemonChiffon1"))
    lVideos[len(lVideos)-1][0].pack()
    lVideos[len(lVideos)-1][1].grid(row=0, column=0, sticky="nsew")
    lVideos[len(lVideos)-1][2].image=pngTN
    lVideos[len(lVideos)-1][2].grid(row=0, column=1, sticky="nsew")
    lVideos[len(lVideos)-1][0].grid_columnconfigure(0, weight=2, uniform="group1")
    lVideos[len(lVideos)-1][0].grid_columnconfigure(1, weight=1, uniform="group1")

#Canvas Botones pack
btnBotones = Button(cBotones, highlightthickness=0, image=pngPlus, bg="DarkOliveGreen1", bd = 0, command=Agregar)
btn2Botones = Button(cBotones, highlightthickness=0, image=pngDown, bg="RoyalBlue1", bd = 0)
btnBotones.grid(row=0, column=0, sticky="nsew")
btn2Botones.grid(row=0, column=1, sticky="nsew")
cBotones.grid_columnconfigure(0, weight=1, uniform="group1")
cBotones.grid_columnconfigure(1, weight=1, uniform="group1")
cBotones.grid_rowconfigure(0, weight=1)

#Canvas Creditos
cCreditos = Canvas(win, bg="grey20", highlightthickness=0)
cCreditos.pack(fill="x")
lblCreditos = Label(cCreditos, text="Jeffry Samuel Eduarte Rojas | Tentri#5008", font="Arial, 8", fg="snow", bg="grey20").pack(anchor="center")
win.mainloop()
