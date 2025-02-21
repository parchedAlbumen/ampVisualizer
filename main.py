import pygame
import numpy as np  
from utility import Utility as use
import audio_processing as aud
import visual_feautures as vf
from button import Button as butt

# animation parts
pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("What yo mama sound like")
clock = pygame.time.Clock()
FPS = 30

#buttons
pause_button = butt("images/WAIT.jpg", (650, 100))
bw_button = butt("images/backward.png", (650,300))
fw_button = butt("images/forward.webp", (650, 500))
cont_button = butt("images/muah.webp", (1000,800))

#values
circleX = 350
circleY = 400
radius = 10.0 #change this to the specific amplitude i want 
active = True

#skipVal
skipVal = 0

#for pause and unpause button
is_paused = False

#allows the song to be played here
pygame.mixer.music.load("song_files/jenieve.mp3")
pygame.mixer.music.play()

while active:  #while playing 
    current_time = pygame.mixer.music.get_pos()/1000 

    window.fill((0,0,0))
    #drawing buttons 
    if is_paused:
        cont_button.draw(window)
    else:
        pause_button.draw(window)

    bw_button.draw(window)
    fw_button.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

        if event.type == pygame.MOUSEBUTTONUP: 
            if pause_button.is_pressed(event):
                pygame.mixer_music.pause()
                is_paused = True    
                cont_button.changePos((650,100))
                pause_button.changePos((1000,800))
            
            elif cont_button.is_pressed(event):
                pygame.mixer_music.unpause()
                is_paused = False
                cont_button.changePos((1000,800))
                pause_button.changePos((650,100))

            if fw_button.is_pressed(event): #skip button
                if (skipVal + 2.5) + current_time > aud.duration:
                    pygame.mixer_music.rewind()
                skipVal += 2.5
                pygame.time.delay(500) 
                pygame.mixer_music.set_pos(current_time + skipVal)

            if bw_button.is_pressed(event): #rewind button
                if (skipVal - 2.5) + current_time <= 1:
                    skipVal = -current_time
                    pygame.mixer_music.rewind()
                else:
                    skipVal -= 2.5
                pygame.time.delay(500)
                pygame.mixer_music.set_pos(current_time + skipVal)

        if event.type == pygame.KEYDOWN: #to continue the game
            if event.key == pygame.K_o:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_p:
                pygame.mixer.music.pause()
            if event.key == pygame.K_d:   #go forward 2 seconds
                if skipVal + 2.5 > aud.duration:
                    pygame.mixer_music.rewind()  #reloop yaheard
                skipVal += 2.5
                pygame.mixer_music.set_pos(current_time + skipVal)
                pygame.time.delay(500)
            if event.key == pygame.K_a:  #to go backwards 
                if (skipVal - 2.5) + current_time <= 0:
                    pygame.mixer_music.rewind()
                    skipVal = -current_time
                else:
                    skipVal -= 2.5
                pygame.time.delay(500)

    current_sec = current_time + skipVal

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

#add more designs on the waveform by adding more letters on ts
#fix forward and skip button, because they seem to have big big problems
#delay 500

