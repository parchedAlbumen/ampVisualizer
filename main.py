import librosa
import matplotlib.pyplot as plt
import pygame
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

#converts the frequencies to decibels
decibel_array_singer = use.convertToDecibel(max_freq_array_singer)
decibel_array_instrumental = use.convertToDecibel(max_freq_array_instrumental)

theRealLebronJamesArray = []
slicing_size = 75
start = 0
for i in range(start, instrumental_spectro.shape[0], slicing_size):
    if (start + slicing_size > instrumental_spectro.shape[0]):
        end = instrumental_spectro.shape[0] - 1
    else:
        end = start + slicing_size
    theRealLebronJamesArray.append(instrumental_spectro[start:end,:])
    start += slicing_size

max_dec_per_array = []
for leArray in theRealLebronJamesArray:
    max_dec_per_array.append(use.convertToDecibel(use.createMaxNpArray(leArray)))

#change the time frame into an array of time
time_array = librosa.frames_to_time(range(vocal_spectro.shape[1]), sr=sr)

#dont mind
circle_y_list = [150,200,250,300,350,400,450,500,550,600,650]

# animation parts
pygame.init()
pygame.mixer.init()

#allows the song to be played here
pygame.mixer.music.load("song_files/jenieve.mp3")
pygame.mixer.music.play()

window = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

#probably should change all the (255,255,255), to whites lol
text_for_vocal = pygame.font.SysFont("vocal: ", 32)
vocal_img = text_for_vocal.render("vocal: ", True, (255,255,255))
text_for_instrumental = pygame.font.SysFont("instrumentals: ", 32) 
instrumental_img = text_for_instrumental.render("instrumentals: ", True,(255,255,255))
text_for_lowest = pygame.font.SysFont("lowest hertz", 30)
lowest_img = text_for_lowest.render("lowest", True, (255,255,255)) 
text_for_highest = pygame.font.SysFont("highest hertz", 30)
highest_img = text_for_highest.render("highest", True, (255,255,255))

circleX = 350
circleY = 400
radius = 10.0 #change this to the specific amplitude i want 

#continue in making the song and change of decibel to match 
active = True
while active:  #while playing 
   #event handling part
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    #texts
    window.blit(vocal_img, (315, 300))
    window.blit(instrumental_img, (575, 75))
    window.blit(lowest_img, (530, 150))
    window.blit(highest_img, (525,650))

    current_time = pygame.time.get_ticks()
    current_sec = current_time / 1000 #convert to milisec for time array (in seconds) 

    #grabs the closest index that represents both each time
    decibel_index = np.searchsorted(time_array, current_sec) 

    singer_radius = float(decibel_array_singer[decibel_index])
    instrumental_radius = float(decibel_array_instrumental[decibel_index])   #going to make use of this, i think

    color = use.random_col(instrumental_radius + 5) #red = loud, blue = moderate, green = quiet 

    pygame.draw.circle(window,(250,250,250),(circleX,circleY), 5 + singer_radius) # draws vocal circle
    
    # pygame.draw.circle(window,color,(350, circleY), 5 + instrumental_radius) #draws instrumental circle <- le current right now 
    pygame.display.flip() #this is the thingy that updates it
    clock.tick(60)

pygame.quit

#make a playback bar thingy so that I can skip stuff 
#try drawing the cirles now, make it look like trapnation vids lol
