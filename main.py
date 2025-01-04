import librosa
import matplotlib.pyplot as plt
import pygame
import numpy as np
import random

vocal_file = "vocal.wav"
song_file = "saturn.mp3"

#used to extract vocal and instrumental from each other
# from audio_separator.separator import Separator
# # Initialize the Separator class (with optional configuration properties, below)
# separator = Separator()
# # Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
# separator.load_model()
# # Perform the separation on specific audio files without reloading the model
# output_files = separator.separate(le_file)
# print(f"Separation complete! Output file(s): {' '.join(output_files)}")   

def random_col():
    rand = random.randint(1, 4)
    match rand:
        case 1:
            return (200,200,200)
        case 2:
            return (100, 0 , 100)
        case 3: 
            return (0,0,200)
        case _:
            return (0,200,10)

y, sr = librosa.load(vocal_file)

#convert to spectro 
spectro = np.abs(librosa.stft(y))

#creates a simple list so I can append later
max_freq_array_singer = []
#grabs the highest frequency from 60hz to 260hz because I think the range of any normal singers 
for i in range(spectro.shape[1]):
    highest_freq = np.max(np.abs(spectro[6:45, i])) #idk why its not [][]
    max_freq_array_singer.append(highest_freq)

max_freq_array_singer = np.array(max_freq_array_singer) 
#these values are in frequencies, so convert to decibels, please 

#converts the frequencies to decibels
decibel_array_singer = np.abs(librosa.amplitude_to_db((max_freq_array_singer)))

#change the time frame into an array of time
time_array = librosa.frames_to_time(range(spectro.shape[1]), sr=sr)
#animation parts
pygame.init()
pygame.mixer.init()

#allows the song to be played here
pygame.mixer.music.load(song_file)
pygame.mixer.music.play()

window = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

circleX = 250
circleY = 250
radius = 10.0 #change this to the specific amplitude i want 

active = True

#continue in making the song and change of decibel to match 
while active:  #while playing 
   #event handling part
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    current_time = pygame.time.get_ticks()
    current_sec = current_time / 1000 #convert to milisec for time array (in seconds) 

    #grabs the closest index that represents both each time
    decibel_index = np.searchsorted(time_array, current_sec) 
    radius = float(decibel_array_singer[decibel_index])

    pygame.draw.circle(window,(100,100,100),(circleX,circleY), radius) # DRAW SINGER CIRCLE

    pygame.display.flip()

    clock.tick(60)

pygame.quit

