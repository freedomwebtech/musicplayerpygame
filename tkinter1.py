from tkinter import *
from search import music, music1
    

win = Tk()
win.geometry('320x100');win.title('Freedomtech Player')
button = Button(win, text="Request Song", command = music )
button.pack()
btn = Button(win, text = 'Pause,Resume,Stop',command = music1)
btn.pack(side='top') 
win.mainloop()

