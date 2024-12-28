import librosa
import matplotlib.pyplot as plt
import numpy as np
import pygame

#time series - an audio signal denoted by y; y[t] is amplitude of the waveform at sample t
#sampling rate - number of samples per second of a time series ??
y, sr = librosa.load("mhmhmm.mp3")

spectro = np.abs(librosa.stft(y))
# print(spectro)

#creates a simple list so I can append later
max_freq_array = []
#grabs the highest frequency from 60hz to 260hz because I think the range of any normal singers 
for i in range(spectro.shape[1]):
    highest_freq = np.max(np.abs(spectro[6:27, i])) #idk why its not [][]
    max_freq_array.append(highest_freq)

max_freq_array = np.array(max_freq_array)  #yep I think i am satisfied with these values 
#these values are in frequencies, so convert to decibels, please 

#converts the frequencies to decibels
decibel_array = np.abs(librosa.amplitude_to_db(np.abs(max_freq_array)))

# grabs the tempo and beat frame (wtv beatframe mean)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

duration = librosa.get_duration(y=y, sr=sr)

#change the time frame into an array of time
time_array = librosa.frames_to_time(range(spectro.shape[1]), sr=sr)

#animation parts
pygame.init()
pygame.mixer.init()

#allows the song to be played here
pygame.mixer.music.load("mhmhmm.mp3")
pygame.mixer.music.play()

window = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

red = (200,200,200)

circleX = 250
circleY = 250
radius = 10 #change this to the specific amplitude i want 

active = True

#continue in making the song and change of decibel to match 
while active:  #while playing 
   #event handling part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    current_time = pygame.time.get_ticks()
    current_sec = current_time / 1000 #because current_time gets mili second

    #i dont get really get this numpy part 
    decibel_index = np.searchsorted(time_array, current_sec) 
    
    pygame.draw.circle(window,red,(circleX,circleY), radius) # DRAW CIRCLE

    pygame.display.flip()

    clock.tick(60)

pygame.quit

#i want to produce 1 bubble per tempo, animation style 
#each beat represents a decibel, the decibel tells you how big the circle is going to be 
