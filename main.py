import librosa

#converts the file to time series and sampling rate (whatever these means)
#time series - an audio signal denoted by y; y[t] is amplitude of the waveform at sample t???
#sampling rate - number of samples per second of a time series ??
y, sr = librosa.load("mhmhmm.mp3")

#grabs the tempo and beat frame (wtv beatframe mean)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(beat_frames)

#duration 
duration = librosa.get_duration(y=y, sr=sr)
# print(duration)

#beat_time is what
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print("hello kadabra!") 
print("WASSUasdasdsadsaP")
