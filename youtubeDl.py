#!/usr/bin/python3
from __future__ import unicode_literals
import youtube_dl
import os
import shutil
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("url", help="url de la vidéo à télécharger",
                    type=str)
parser.add_argument("--son", help="url de la musique à télécharger", action="store_true")
parser.add_argument("--video", help="url de la vidéo à télécharger", action="store_true")
args=parser.parse_args()

if args.son:
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

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([args.url])

        
        for element in os.listdir('.'):
            if element.endswith('.mp3'):
                os.rename("%s"  % element, "/home/altins/Téléchargements/%s" % element)
                print("Votre fichier à étais enregistrer dans votre dossier téléchargement")
        
        break

if args.video:

    ydl_opts = {}    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])
    
    print("vidéo bien télécharger, transfert en cours...")
    for element in os.listdir('.'):
            if element.endswith('.mkv'):
                os.rename("%s"  % element, "/home/altins/Téléchargements/%s" % element)
                print("Votre fichier à étais enregistrer dans votre dossier téléchargement")

