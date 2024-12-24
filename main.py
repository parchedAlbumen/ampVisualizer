import librosa
import matplotlib.pyplot as plt
import numpy as np

#time series - an audio signal denoted by y; y[t] is amplitude of the waveform at sample t
#sampling rate - number of samples per second of a time series ??
y, sr = librosa.load("mhmhmm.mp3")

spectro = np.abs(librosa.stft(y))
# print(spectro)

max_freq_array = np.array([])

#very very wrong, each spectro[index] represents the OVERALL frequency for that range of hertz
#I want to see how the hertz progress OVER TIME not find the highest frequency at the specific hertz
#meaning, "go play with the [][] second dimension of spectro, because it shows you the progress over time"
#----------------------------------------------------------------------------
# for i in range(0, spectro.shape[1]):
#     if (i == spectro.shape[1]): 
#         print("Hallo")
#     else: 
#         max_freq = np.max(np.abs(spectro[i]))
#         np.append(max_freq_array, max_freq)

print(np.max(spectro[0]))
# print(max_freq_array)
# #let's check if its arraying like how i want it to array
# for i in max_freq_array:
#     print(i + '\n')

# for i in range(1,50):
#     print(max_freq_array[i])
#----------------------------------------------------------------------------
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
