import os, sys, pip
from pytube import YouTube, Playlist
print("Instant Music by Tentri#5008")
carp = "/storage/emulated/0/Dowload"

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
            print("Error\n Puede ser causado por una actualización pendiente, desea verificar actualizaciones? (S/N)")
            opc = input()
            if opc=="s" or opc=="S":
                if hasattr(pip, 'main'): pip.main(['install', 'pytube', '-U'])
                else: pip._internal.main(['install', 'pytube', '-U'])
            else: exit()
            print("Listo, porfavor reinicie la aplicación")
            input()
            exit()
get(input())
