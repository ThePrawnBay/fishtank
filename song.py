import pygame
import time
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("music example")


pygame.mixer.music.load('hungry-shark-background-music.wav')
sound_effect = pygame.mixer.Sound('1-01. Bikini Bottom.wav')
effect_sound = pygame.mixer.Sound('jaws_x.wav')


pygame.mixer.music.play(-1) #the -1 argument makes the music loop indefinitly


while 1:
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            time.sleep(60) # wait and let the sound play for # second
            effect_sound.stop()
            
        elif keys[pygame.K_w]: #Press w to play song
            effect_sound.play()
            time.sleep(60) # wait and let the sound play for # second
            effect_sound.stop()
            
        elif event.type == pygame.MOUSEBUTTONDOWN: #Click mouse to play song
            sound_effect.play()
            time.sleep(60) # wait and let the sound play for # second
            effect_sound.stop()
            
            
pygame.quit
