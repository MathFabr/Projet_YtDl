#!/usr/bin/python3
from __future__ import unicode_literals
import youtube_dl
import os
import shutil

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

while (1==1) :
    url=input("Entrer l'url de la vidéo don vous voulez récupérer le son: ")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # os.rename("*.mp3", "home/altins/Téléchargements/*.mp3")
    

    cont=input("Voulez vous récupérer un autre son? O/n")

    if (cont=='n'):
        break