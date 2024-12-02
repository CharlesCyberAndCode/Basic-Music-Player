## Basic Music Player

import tkinter as tk 
from tkinter import *
from tkinter import filedialog
import os
import pygame
from PIL import ImageTk 
pygame.init()

window = tk.Tk()
window.title("Music Player")
canvas = tk.Canvas (window, width = 441, height = 256, bg = "blue")
image = ImageTk.PhotoImage(file = r"C:\python\Music Player\download.png")
canvas.create_image(1, 1, image = image, anchor = NW)

# Globals

playing = True
playlist = []
currentSong = "Song Name"

# Function for music

def playMusic():
    global currentSong   
    filePath = filedialog.askopenfilename(filetypes=[("Audio Files" , ".mp3")])
    baseName = os.path.basename(filePath)
    name, ext = os.path.splitext(baseName)
    label.config(text = name)
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play()
    print(currentSong)

def pauseMusic():
    pygame.mixer.music.pause()

def unpauseMusic():
    pygame.mixer.music.unpause()

def spacebar(event):
    global playing
    if playing == True:
        pauseMusic()
        playing = False
        
    else:
        unpauseMusic()
        playing = True
        

songEnd = pygame.USEREVENT + 1 
pygame.mixer.music.set_endevent(songEnd)

canvas.bind("<space>", spacebar) 
canvas.focus_set()  
# Buttons etc. here


playButton = tk.Button(window , text = "Play Music" , command = playMusic)
playButton.pack()

pauseButton = tk.Button(window , text = "Pause" , command = pauseMusic)
pauseButton.pack()

resumeButton = tk.Button(window , text = "Play Music" , command = unpauseMusic)
resumeButton.pack()

label = tk.Label(window, text = currentSong)
label.place(relx = .5, rely = .6, anchor = tk.CENTER)
playButtonWindow = canvas.create_window(220, 50, window = playButton)
pauseButtonWindow = canvas.create_window(220, 75, window = pauseButton)
resumeButton = canvas.create_window(220, 100, window = resumeButton)
canvas.pack()
# main 
window.mainloop()