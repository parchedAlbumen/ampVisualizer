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
print(type(spectro.shape[1])) #total amount of time frame is 7315

#grabs the highest frequency from 60hz to 260hz because I think the range of any normal singers 
for i in range(spectro.shape[1]):
    highest_freq = np.max(np.abs(spectro[6:27, i])) #idk why its not [][]
    max_freq_array.append(highest_freq)

max_freq_array = np.array(max_freq_array)  #yep I think i am satisfied with these values 
#these values are in frequencies, so convert to decibels, please 

#NEXT GOAL: convert to decibels, then figure out how to animate the voice 

#convert time series amplitude to decibels   
decibels = abs(librosa.amplitude_to_db(np.abs(spectro)))

# grabs the tempo and beat frame (wtv beatframe mean)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
# print(beat_frames)

#duration 
duration = librosa.get_duration(y=y, sr=sr)
# print(duration)

# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
# for time in beat_times:     
#     sampleSec = librosa.time_to_samples(time, sr=sr)
#     print(sampleSec)


#convert that max maginutde freq array to decibels, so its cooler 
#loudest sound at a point in time 
#i want to produce 1 bubble per tempo, animation style 
#each beat represents a decibel, the decibel tells you how big the circle is going to be 
