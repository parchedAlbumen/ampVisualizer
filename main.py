import librosa
import matplotlib.pyplot as plt
import pygame
import numpy as np
import random

vocal_file = "vocal.wav"
instrumental_file = "saturn_instrumental.wav"

#used to extract vocal and instrumental from each other
# from audio_separator.separator import Separator
# # Initialize the Separator class (with optional configuration properties, below)
# separator = Separator()
# # Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
# separator.load_model()
# # Perform the separation on specific audio files without reloading the model
# output_files = separator.separate(le_file)
# print(f"Separation complete! Output file(s): {' '.join(output_files)}")   

def createMaxNpArray(spectro_array):
    max_freq_array = [] 
    for i in range(spectro_array.shape[1]): 
        highest_freq = np.max(np.abs(spectro_array[:,i])) #selects all frequencies at time i and finds the biggest
        max_freq_array.append(highest_freq)
    return np.array(max_freq_array)

def convertToDecibel(array):
    return np.abs(librosa.amplitude_to_db(array))
    
def random_col(radius):
    if (radius >= 40):
        return (255,0,0)
    elif (radius >= 25):
        return (0,0,255)
    else: 
        return (0,255,0)

def generateRandomY():
    return random.randint(250, 750)

y, sr = librosa.load(vocal_file)
y1, _ = librosa.load(instrumental_file)

#convert to spectro 
vocal_spectro = np.abs(librosa.stft(y)) 
instrumental_spectro = np.abs(librosa.stft(y1))

max_freq_array_singer = createMaxNpArray(vocal_spectro)
max_freq_array_instrumental = createMaxNpArray(instrumental_spectro)

#converts the frequencies to decibels
decibel_array_singer = convertToDecibel(max_freq_array_singer)
decibel_array_instrumental = convertToDecibel(max_freq_array_instrumental)

theRealLebronJamesArray = []
slicing_size = 100
start = 0
for i in range(start, instrumental_spectro.shape[0], slicing_size):
    if (start + slicing_size > instrumental_spectro.shape[0]):
        end = instrumental_spectro.shape[0] - 1
    else:
        end = start + slicing_size
    theRealLebronJamesArray.append(instrumental_spectro[start:end,:])

print(theRealLebronJamesArray)
#change the time frame into an array of time
time_array = librosa.frames_to_time(range(vocal_spectro.shape[1]), sr=sr)

#animation parts
pygame.init()
pygame.mixer.init()

#allows the song to be played here
pygame.mixer.music.load("saturn.mp3")
pygame.mixer.music.play()

window = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

circleX = 250
circleY = 250
radius = 10.0 #change this to the specific amplitude i want 

#continue in making the song and change of decibel to match 
active = True
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

    singer_radius = float(decibel_array_singer[decibel_index])
    instrumental_radius = float(decibel_array_instrumental[decibel_index])

    color = random_col(instrumental_radius + 5) #red = loud, blue = moderate, green = quiet 

    pygame.draw.circle(window,(250,250,250),(150,circleY), 5 + singer_radius) # draws vocal circle
    # pygame.draw.circle(window,color,(350, circleY), 5 + instrumental_radius) #draws instrumental circle <- le current right now 

    #figure out how to slice the instrumental spectro

    pygame.display.flip() #this is the thingy that updates it
    clock.tick(60)

pygame.quit

#next goal is to separate the time bins 
#make a playback bar thingy so that I can skip stuff 

