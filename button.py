import pygame
import math
class Button:
    def __init__(self, xpos, ypos, width, height, color, text, isPressed= False):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.isPressed = isPressed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, self.width, self.height))
        

    def pressed(self, event, mousePos,count):
        if mousePos[0] > self.xpos and mousePos[0] < self.xpos + self.width and mousePos[1] < self.ypos + self.height and mousePos[1] > self.ypos and event.type == pygame.MOUSEBUTTONDOWN:
            count +=1
            



