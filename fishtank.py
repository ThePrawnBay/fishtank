import pygame
import random
import time
import button



pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock() 
count = 1

class Fish:
    def __init__(self):
        self.fishImage = pygame.image.load("nemo.png").convert_alpha()
        pygame.Surface.set_colorkey (self.fishImage, [255,0,255])
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.speed = 1
        self.xDir = random.randint(-1,1)
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time() #grab starting time

    def move(self):
        # Move the fish
        self.xpos += self.xDir* self.speed
        self.ypos += self.yDir * self.speed

        # Change direction every 3 seconds
        if time.time() - self.last_change_time > 3:  
            self.xDir = random.randint(-1,1)
            self.yDir = random.randint(-1,1)
            self.last_change_time = time.time() #reset the time

        # Check for collision with walls and change direction
        if self.xpos <= 0 or self.xpos >= 750:
            self.xDir *= -1
        if self.ypos <= 0 or self.ypos>= 550:
            self.yDir *= -1

    def draw(self, screen):
        screen.blit(self.fishImage, (self.xpos, self.ypos))

def AddFish(button,count):
    if button.pressed(event, mousePos,count):
        print(count)


        


# instantiate a fish object


addbutton= button.Button(600,200,20,20,(255,255,255), 'hello')




# player variables


fish = []
for i in range(count): 
    fish.append(Fish())



running = True
while running:# Game loop########################################################
    clock.tick(60)
    #input/event section-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #physics/update section--------------------------
    mousePos = pygame.mouse.get_pos()
    AddFish(addbutton,count)


  


    #render section----------------------------------
    # Fill the screen with a background color
    screen.fill((0, 150, 255))

    # Draw the fish

    for i in range(len(fish)):
        fish[i].draw(screen)
        fish[i].move()
    addbutton.draw(screen)


    # Update the display
    pygame.display.flip()

    #end of game loop!#######################################################

pygame.quit()