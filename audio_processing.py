import librosa
import numpy as np  
from utility import Utility as use

vocal_file = "song_files/jen_vocals.wav"
instrumental_file = "song_files/jen_instrumental.wav"

y, sr = librosa.load(vocal_file)
y1, _ = librosa.load(instrumental_file)

#convert to spectro 
vocal_spectro = np.abs(librosa.stft(y)) 
instrumental_spectro = np.abs(librosa.stft(y1))

max_freq_array_singer = use.createMaxNpArray(vocal_spectro)
max_freq_array_instrumental = use.createMaxNpArray(instrumental_spectro)

decibel_array_singer = use.convertToDecibel(max_freq_array_singer)
decibel_array_instrumental = use.convertToDecibel(max_freq_array_instrumental)

divided_instrumentals = []  # array for the instrumentals 
slicing_size = 75 
start = 0
for i in range(start, instrumental_spectro.shape[0], slicing_size):
    if (start + slicing_size > instrumental_spectro.shape[0]):
        end = instrumental_spectro.shape[0] - 1
    else:
        end = start + slicing_size
    divided_instrumentals.append(instrumental_spectro[start:end,:])
    start += slicing_size

max_dec_per_array = []
for leArray in divided_instrumentals:
    max_dec_per_array.append(use.convertToDecibel(use.createMaxNpArray(leArray)))

time_array = librosa.frames_to_time(range(vocal_spectro.shape[1]), sr=sr)

