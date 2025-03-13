import pygame, sys




class Bubble(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('Bubble 1.png'))
        self.sprites.append(pygame.image.load('Bubble 2.png'))
        self.sprites.append(pygame.image.load('Bubble 3.png'))
        self.sprites.append(pygame.image.load('Bubble 4.png'))
        self.sprites.append(pygame.image.load('Bubble 5.png'))
        self.sprites.append(pygame.image.load('Bubble 6.png'))
        self.sprites.append(pygame.image.load('Bubble 7.png'))
        self.sprites.append(pygame.image.load('Bubble 8.png'))
        self.sprites.append(pygame.image.load('Bubble 9.png'))
        self.sprites.append(pygame.image.load('Bubble 10.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [xpos,ypos]

    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.3

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("sprite animation")

moving_sprites = pygame.sprite.Group()
Bubble = Bubble(50,50)
moving_sprites.add(Bubble)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            Bubble.animate() 


    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)