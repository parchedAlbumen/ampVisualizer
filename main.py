import librosa
import matplotlib.pyplot as plt
import numpy as np

#time series - an audio signal denoted by y; y[t] is amplitude of the waveform at sample t
#sampling rate - number of samples per second of a time series ??
y, sr = librosa.load("mhmhmm.mp3")

spectro = np.abs(librosa.stft(y))
print(spectro)

max_freq_array = np.array([])

for t in range(spectro.shape[1]): 
    max_freq = np.max(np.abs(spectro[:, t]))
    np.append(max_freq_array, max_freq)

#let's check if its arraying like how i want it to array
for i in max_freq_array:
    print(i) 

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
