import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock()

# Initialize font for score
font = pygame.font.SysFont(None, 36)

score = 0
money = 0
class Fish:
    def __init__(self):
        self.fishImage = pygame.image.load("nemo.png").convert_alpha()
        pygame.Surface.set_colorkey(self.fishImage, [255, 0, 255])
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.speed = 10
        self.xDir = random.randint(-1, 1)
        self.yDir = random.randint(-1, 1)
        self.last_change_time = time.time()
        self.sold = False

    def move(self):
        self.xpos += self.xDir * self.speed
        self.ypos += self.yDir * self.speed
        if time.time() - self.last_change_time > 3:
            self.xDir = random.randint(-1, 1)
            self.yDir = random.randint(-1, 1)
            self.last_change_time = time.time()

        if self.xpos <= 0 or self.xpos >= 750:
            self.xDir *= -1
        if self.ypos <= 0 or self.ypos >= 550:
            self.yDir *= -1

    def draw(self, screen):
        screen.blit(self.fishImage, (self.xpos, self.ypos))

    def sell(self, shop_rect):
        if shop_rect.collidepoint(self.xpos, self.ypos) and not self.sold:
            self.sold = True
            return True
        return False


class Shop:
    def __init__(self):
        self.shopImage = pygame.image.load("shop.jpg").convert_alpha()
        pygame.Surface.set_colorkey(self.shopImage, [255, 0, 255])
        self.shop_rect = self.shopImage.get_rect()
        self.shop_rect.topleft = (550, 430)
        

    def draw(self, screen):
        screen.blit(self.shopImage, self.shop_rect.topleft)

    def get_rect(self):
        return self.shop_rect


# Initialize the Fish and Shop objects
shop = Shop()
fish = Fish()
# Initialize score variable
score = 0

running = True
while running:  # Game loop
    clock.tick(60)
    
    # Input/event section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Physics/update section
    fish.move()

    # Check if fish collides with the shop to "sell" it
    if fish.sell(shop.get_rect()):
        # Increment the score when the fish is sold
        score += 1
        money += 10
        print("Fish sold! Score:", score)
        print("Fish sold! Money:", money)
        fish = Fish()  # Generate a new fish after selling

    # Render section
    screen.fill((0, 150, 255))  # Fill screen with background color

    # Draw the fish and shop
    fish.draw(screen)
    shop.draw(screen)

    # Display score
    score_text = font.render("Score: ", score, True, (255, 255, 255))  # White text
    screen.blit(score_text, (10, 10))  # Display score in the top-left corner
    
    score_text = font.render("Money: ", money, True, (255, 255, 255))  # White text
    screen.blit(score_text, (10, 50))  # Display score in the top-left corner


    
    # Update the display
    pygame.display.flip()

# End of game loop!
pygame.quit()
