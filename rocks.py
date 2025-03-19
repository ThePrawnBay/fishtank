import pygame
import random
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

class Snowflake:
    def __init__(self, x, y):# constructer
        self.xpos = x
        self.ypos = y
    def move(self):
        self.xpos += random.randrange(-9, 10)# left + right
        self.ypos += random.randrange(-3, 1)# up + down
        if self.ypos < 700:
            self.ypos = random.randrange(700, 800)# resets snowflakes
    def draw(self):
        pygame.draw.circle(screen, (157, 16, 25), (self.xpos, self.ypos),random.randrange(5,10))
        pygame.draw.circle(screen, (235, 80, 90), (self.xpos, self.ypos),random.randrange(4,5))


#create a buncha empty lists
sizes1 = []
positions1 = []
colors1 = []
sizes2 = []
positions2 = []
colors2 = []

flakeBag = []# snowflake list
for i in range(30):
    flakeBag.append(Snowflake(random.randrange(0, 800), random.randrange(700, 800)))# makes snowflakes

#push a buncha numbers into the lists
for i in range(1500):
    sizes1.append(random.randrange(7,20)) #push in 1 number
    positions1.append((random.randrange(0, 800),random.randrange(700, 800))) #push in a 2-slot TUPLE
    colors1.append((random.randrange(160,255),26,28)) #push in a 3-slot TUPLE
    sizes2.append(random.randrange(1,15)) #push in 1 number
    positions2.append((random.randrange(0, 800),random.randrange(700, 800))) #push in a 2-slot TUPLE
    colors2.append((random.randrange(100,110),16,18)) #push in a 3-slot TUPLE

while(1): #omg game lup---------
    clock.tick(60) #FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #physics section----
    
    #move flakes
    for i in range(len(flakeBag)):
        flakeBag[i].move()

    #render section---
    screen.fill((135,206,235))

    for i in range(1000):
        pygame.draw.circle(screen, colors1[i], (positions1[i][0], positions1[i][1]), sizes1[i])
    for n in range(500):
        pygame.draw.circle(screen, colors2[n], (positions2[n][0], positions2[n][1]), sizes2[n])


    for i in range(len(flakeBag)):# draws snowflakes
        flakeBag[i].draw()
 
    
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()