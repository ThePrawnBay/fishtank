import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("music example")


pygame.mixer.music.load('Watertank.mp3') 
sound_effect = pygame.mixer.Sound('bubbling2.wav')  

pygame.mixer.music.play(-1)  # The '-1' argument makes the music loop indefinitely


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sound_effect.play()


pygame.quit()