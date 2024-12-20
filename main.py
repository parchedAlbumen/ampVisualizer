import librosa
import matplotlib.pyplot as plt
#converts the file to time series and sampling rate (whatever these means)
#time series - an audio signal denoted by y; y[t] is amplitude of the waveform at sample t???
#sampling rate - number of samples per second of a time series ??

print("started")
y, sr = librosa.load("mhmhmm.mp3", duration=10)

#convert time series amplitude to decibels  
decibels = abs(librosa.amplitude_to_db(abs(y)))

print("ended")

# grabs the tempo and beat frame (wtv beatframe mean)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
# print(beat_frames)

#duration 
duration = librosa.get_duration(y=y, sr=sr)
# print(duration)

#beat_time is what
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
for time in beat_times:     
    sampleSec = librosa.time_to_samples(time, sr=sr)
    print(sampleSec)

#loudest sound at a point in time 


#i want to produce 1 bubble per tempo, animation style 
#each beat represents a decibel, the decibel tells you how big the circle is going to be 
