import librosa
import numpy as np  
from .utility import Utility as use

vocal_file = "song_files/vocals_output.wav"
instrumental_file = "song_files/instrumentals_output.wav"

#load files
y, sr = librosa.load(vocal_file)
y1, _ = librosa.load(instrumental_file)
duration = librosa.get_duration(y=y, sr=sr)

#converts to magnitudes of each frame in the spectograms
vocal_spectro = np.abs(librosa.stft(y)) 
instrumental_spectro = np.abs(librosa.stft(y1))

#creates an array of most significant magnitudes per time frame
max_freq_array_singer = use.createMaxNpArray(vocal_spectro)
max_freq_array_instrumental = use.createMaxNpArray(instrumental_spectro)

#converts each frequencies into decibel
decibel_array_singer = use.convertToDecibelSinger(max_freq_array_singer)
#AFTER FIXING SINGER ARRAY WORK ON INSTRUMENTALS (create functions and clean it up)
decibel_array_instrumental = use.convertToDecibelInstrumentals(max_freq_array_instrumental)

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
    max_dec_per_array.append(use.convertToDecibelInstrumentals(use.createMaxNpArray(leArray)))

time_array = librosa.frames_to_time(range(vocal_spectro.shape[1]), sr=sr)

#FOR PROCESSING THE DATA SO IT CAN TURN INTO THE BUMPS