from pytube import YouTube
from moviepy.editor import * 
import os,shutil

def get_mp3():
    url = input("Lütfen Youtube linkini giriniz : ")
    output = input("Hangi formatta indirmek istersiniz ? (wav/mp3) : ")
    print("Converting....")

    mp4= YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4",1)[0] + f".{output}"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()

    #if you want to save the mp4 format,you need to delete it
    os.remove(mp4) 
    

get_mp3()    