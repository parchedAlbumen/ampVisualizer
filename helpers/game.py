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
    music_button = butt("images/lebutton.jpg",(WIDTH//2 - 150, 300))
    info_button = butt("images/lebutton.jpg",(WIDTH//2 - 150, 450))
    back_button = butt("images/lebutton.jpg",(50,50))

    #for the songs running
    skipVal = 0.0
    is_paused = False   
    song_loaded = False #???

    curr_state = MENU
    active = True

    def create_text(s, xy, size=30):
        font = pygame.font.SysFont(None, size)
        surf = font.render(s, True, (220, 220, 220))
        window.blit(surf, xy)

    #idk if i even need a helper ngl
    while active: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if curr_state in (INFO, PLAY): #check if we aren't in the menu already
                        if curr_state == PLAY:
                            pygame.mixer.music.stop() #i guess this also resets the song
                        is_paused = False #wha should it not be true here?
                        skipVal = 0.0
                        curr_state = MENU
            
            if curr_state == MENU and event.type == pygame.MOUSEBUTTONUP:
                if music_button.is_pressed(event):
                    #check
                    if not song_loaded:
                        pygame.mixer.music.load("song_files/ogAudio.wav")
                        song_loaded = True
                    pygame.mixer.music.play()
                    is_paused = False
                    skipVal = 0.0
                    curr_state = PLAY
                
                elif info_button.is_pressed(event):
                    curr_state = INFO

            elif curr_state == INFO and event.type == pygame.MOUSEBUTTONUP:
                if back_button.is_pressed(event):
                    curr_state = MENU
            
            elif curr_state == PLAY:
                if event.type == pygame.MOUSEBUTTONUP: 
                    if pause_button.is_pressed(event):
                        pygame.mixer.music.pause()
                        is_paused = True    
                        cont_button.changePos((650,100))
                        pause_button.changePos((1000,800))
                
                    elif cont_button.is_pressed(event):
                        pygame.mixer.music.unpause()
                        is_paused = False
                        cont_button.changePos((1000,800))
                        pause_button.changePos((650,100))
      
                    if fw_button.is_pressed(event): #skip button
                        curr_time = pygame.mixer.music.get_pos() / 1000 #get current time 
                        if (skipVal - 2.5) + curr_time > aud.duration: #if value is greater than the whole song, restart
                            pygame.mixer.music.rewind()
                            skipVal = -curr_time

                        skipVal += 2.5
                        pygame.time.delay(120) #to avoid spamming 
                        pygame.mixer.music.set_pos(curr_time + skipVal)

                    if bw_button.is_pressed(event): #rewind button
                        curr_time = pygame.mixer.music.get_pos() / 1000 
                        if (skipVal - 2.5) + curr_time <= 0:
                            skipVal = -curr_time
                            pygame.mixer.music.rewind()
                        else:
                            skipVal -= 2.5
                        pygame.time.delay(500)
                        pygame.mixer.music.set_pos(curr_time + skipVal)

        window.fill((0,0,0))
        if curr_state == MENU:
            create_text("Music Visualizer", (40, 40), size=48)
            create_text("Press a button:", (40, 120), size=32)
            music_button.draw(window)
            info_button.draw(window)
            create_text("Start", (40, 160), 32)
            create_text("Info",  (40, 200), 32) #40 and 200 are x and y positions
            create_text("Tip: ESC returns here from any screen.", (40, HEIGHT - 60), 24)

        elif curr_state == INFO:
            create_text("leave this for now lol", (40,40), size=48)

        elif curr_state == PLAY:
            current_time = pygame.mixer.music.get_pos() / 1000.0
            current_sec = current_time + skipVal

            if is_paused:
                cont_button.draw(window)
            else:
                pause_button.draw(window)

            bw_button.draw(window)
            fw_button.draw(window)

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

            create_text(f"t={current_sec:0.2f}s  (paused={is_paused})", (20, 20), 24)
            create_text("ESC=Menu", (20, 50), 24)
                    
        pygame.display.flip() #this is the thingy that updates it
        clock.tick(60)
    
    pygame.quit

#goals:
#improve instrumental visualizer
#put some threshold in the vocals
#make everything look more pretty 
#clean up
#after all these r done, add essentia features xddxdxdx