import os
import pygame, mutagen.mp3
import glob
import subprocess
from ai import audio,speak

def music():
    a=audio().replace(" ","")      
    os.system('sudo youtube-dl -o "%(autonumber)s-%("song")s.%(ext)s" -x --audio-format mp3 ytsearch:'+ a) 

    d=str(glob.glob('00001-NA.mp3')).replace("[","").replace("]","").replace("'","")

    speak("Sir Playing" +a)
    
    
    
  
    mp3 = mutagen.mp3.MP3(d)
    pygame.mixer.init(frequency=mp3.info.sample_rate)
    pygame.mixer.music.load(d)
    pygame.mixer.music.set_volume(40)
    pygame.mixer.music.play()
    
    
def music1():
    query=audio()
    if query == 'pause':
       pygame.mixer.music.pause()
    if query == "resume":
       pygame.mixer.music.unpause()    
    if query == "stop song":
       pygame.mixer.music.stop()
            



    