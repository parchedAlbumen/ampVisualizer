import librosa
import matplotlib.pyplot as plt
import numpy as np

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

#NEXT GOAL: I WANT TO GRAB THE SPECIFIC DECIBEL PER TIME FRAME USING THE BEAT TIME, so convert beat time to frames first, and
#figure out a way to find the time frame
#and figure out how to animate the voice 
#duration
duration = librosa.get_duration(y=y, sr=sr)

# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
# for time in beat_times:     
#     sampleSec = librosa.time_to_samples(time, sr=sr)
#     print(sampleSec)


#convert that max maginutde freq array to decibels, so its cooler 
#loudest sound at a point in time 
#i want to produce 1 bubble per tempo, animation style 
#each beat represents a decibel, the decibel tells you how big the circle is going to be 
