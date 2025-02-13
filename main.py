import librosa
import matplotlib.pyplot as plt
import pygame
import numpy as np  
from utility import Utility as use
import audio_processing as aud
import visual_feautures as vf

# animation parts
pygame.init()
pygame.mixer.init()

#allows the song to be played here
pygame.mixer.music.load("song_files/jenieve.mp3")
pygame.mixer.music.play()

window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("What yo mama sound like")
clock = pygame.time.Clock()
FPS = 30

circleX = 350
circleY = 400
radius = 10.0 #change this to the specific amplitude i want 

#continue in making the song and change of decibel to match 
active = True
RUNNING, PAUSE = 1,0
currentState = RUNNING
time_paused = 0
time_reran = 0
elapsed_time = 0
while active:  #while playing 
   #event handling part
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN: #to continue the game
            if event.key == pygame.K_o:
                currentState = RUNNING
                pygame.mixer.music.unpause()
                time_reran = pygame.time.get_ticks()
                elapsed_time += time_reran - time_paused
            if event.key == pygame.K_p:  #to pause the game 
                currentState = PAUSE
                time_paused = pygame.time.get_ticks()
                pygame.mixer.music.pause()
    
    if (currentState): #currently running
        time = 0 + elapsed_time
        current_time = pygame.time.get_ticks()  - time
        current_sec = current_time/1000 #convert to milisec for time array (in seconds) 

    #grabs the closest index that represents both each time
        decibel_index = np.searchsorted(aud.time_array, current_sec) 

        singer_radius = float(aud.decibel_array_singer[decibel_index])
        instrumental_radius = float(aud.decibel_array_instrumental[decibel_index])   #going to make use of this, i think

        color = use.random_col(instrumental_radius + 5) #red = loud, blue = moderate, green = quiet
        pygame.draw.circle(window,(250,250,250),(circleX,circleY), 5 + singer_radius) # draws vocal circle

        for i in range(0, len(aud.max_dec_per_array)):
            the_current_dec = float(aud.max_dec_per_array[i][decibel_index])
            random_index = use.generateRandomOBlockNum()
            whats_a_father = vf.random_letters_list_for_rest[random_index]
            whatsthat = vf.random_letters_list_for_high[random_index]
            shape_font = pygame.font.SysFont(whats_a_father, 25)

            if the_current_dec <= 12.5:
                shape_img = shape_font.render(whats_a_father, True, (0,255,0))
                window.blit(shape_img, (vf.x_list[i], 245))
            elif the_current_dec <= 25:
                shape_img = shape_font.render(whats_a_father, True, (0,0,255))
                window.blit(shape_img, (vf.x_list[i], 230))
            elif the_current_dec <= 37.5: 
                shape_img = shape_font.render(whats_a_father,  True, (255,150,0))
                window.blit(shape_img, (vf.x_list[i], 215))
            else:
                shape_img = shape_font.render(whats_a_father, True, (255,0,0))
                window.blit(shape_img, (vf.x_list[i], 200))
            
        pygame.display.flip() #this is the thingy that updates it
        clock.tick(60)

pygame.quit

#make skip 5 seconds button
#also clean up code so it looks less stupid
