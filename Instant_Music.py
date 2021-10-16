import os, sys, pip, getpass
from pytube import YouTube, Playlist
print("Instant Music by Tentri#5008")
if os.name == "posix":
    carp = "/storage/emulated/0/Dowload"
else:
    carp = "C:\\Users\\"+getpass.getuser()+"\\Music"

def desc(yt):
    print(yt.title)
    audio = yt.streams.get_audio_only().download(carp)
    base, ext = os.path.splitext(audio)
    audioN = base + '.mp3'
    if os.path.exists(audioN): os.remove(audioN)
    os.rename(audio, audioN)

def get(link):
    try:    desc(YouTube(link))
    except:
        try:
            pl = Playlist(link)
            for c in pl.video_urls: desc(YouTube(c))
        except:
            print("Error\n It may be caused by a pending update, do you want to check for updates? (Y/N)")
            opc = input()
            if opc=="y" or opc=="Y":
                if hasattr(pip, 'main'): pip.main(['install', 'pytube', '-U'])
                else: pip._internal.main(['install', 'pytube', '-U'])
            else: exit()
            print("Done, please restart the application")
            input()
            exit()
print("Link: ", end="")
get(input())
