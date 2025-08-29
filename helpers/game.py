import pygame
import numpy as np  
from .utility import Utility as use
from . import audio_processing as aud
from . import visual_feautures as vf
from .button import Button as butt

#global stuffs
FPS = 60 #?
WIDTH, HEIGHT = 1000, 800

MENU, INFO, PLAY = "menu", "info", "play"   

def run_game():
    pygame.init() #for the game
    pygame.mixer.init() #music

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("What yo mama sound like")
    clock = pygame.time.Clock()

    #buttons for song playing 
    pause_button = butt("images/WAIT.jpg", (650, 100))
    bw_button = butt("images/backward.png", (650,300))
    fw_button = butt("images/forward.webp", (650, 500))
    cont_button = butt("images/muah.webp", (1000,800))

    #make buttons for info/song playing/going back button
    # music_button = butt(,())
    # info_button = butt(,())
    # go_back = butt(,())

    #for the songs running
    skipVal = 0.0
    is_paused = False   
    song_loaded = False #???

    curr_state = MENU
    active = True

    #idk if i even need a helper ngl
        # current_time = pygame.mixer.music.get_pos()/1000

        # window.fill((0,0,0))
        # #drawing buttons 
        # if is_paused:
        #     cont_button.draw(window)
        # else:
        #     pause_button.draw(window)

        # bw_button.draw(window)
        # fw_button.draw(window)
    while active: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if curr_state in (INFO, PLAY): #check if we aren't in the menu already
                        if curr_state == PLAY:
                            pygame.mixer.music.stop()
                        state = MENU
                        is_paused = False #wha  
                        skipVal = 0.0
            
            if curr_state == MENU and event.type == pygame.MOUSEBUTTONUP:
                print("hello")
            if event.type == pygame.MOUSEBUTTONUP: 
                if pause_button.is_pressed(event):
                    pygame.mixer.music.pause()
                    is_paused = True    
                    cont_button.changePos((650,100))
                    pause_button.changePos((1000,800))
                
                if cont_button.is_pressed(event):
                    pygame.mixer.music.unpause()
                    is_paused = False
                    cont_button.changePos((1000,800))
                    pause_button.changePos((650,100))
      
                if fw_button.is_pressed(event): #skip button
                    if (skipVal + 2.5) + current_time > aud.duration:
                        pygame.mixer.music.rewind()
                    skipVal += 2.5
                    pygame.time.delay(500) 
                    pygame.mixer.music.set_pos(current_time + skipVal)
                    #hi

                if bw_button.is_pressed(event): #rewind button
                    if (skipVal - 2.5) + current_time <= 1:
                        skipVal = -current_time
                        pygame.mixer.music.rewind()
                    else:
                        skipVal -= 2.5
                    pygame.time.delay(500)
                    pygame.mixer.music.set_pos(current_time + skipVal)
            current_sec = current_time + skipVal

        #grabs the closest index that represents both each time
        decibel_index = np.searchsorted(aud.time_array, current_sec) 

        singer_radius = float(aud.decibel_array_singer[decibel_index])
        instrumental_radius = float(aud.decibel_array_instrumental[decibel_index])   #going to make use of this, i think

        color = use.random_col(instrumental_radius + 5) #red = loud, blue = moderate, green = quiet
        pygame.draw.circle(window,(250,250,250),(vf.circleX, vf.circleY), 5 + singer_radius) # draws vocal circle

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


