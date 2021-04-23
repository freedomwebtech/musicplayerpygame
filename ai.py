import speech_recognition as sr
from gtts import gTTS
import os
import time
from tkinter import *


def audio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      data = r.recognize_google(audio)
      print(data)
      
    return data
    
def audio1():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      r.adjust_for_ambient_noise(source)
     
      
      audio1 = r.listen(source)
      
#      data1 = r.recognize_google(audio1)
      
     
#      print(data1)
#    return data1
            
def speak(audiostring):
    tts=gTTS(text=audiostring,lang="en")
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    
    
#audio1()
     

  
