import pygame, sys, os
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)


#Step 1: Initialize the Game
pygame.init()



#Step 2: Setup the Window
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('what is the use')#not needed


#Step 3: Setup the Surface
screen = pygame.display.get_surface()
screen.fill(GREEN)
pygame.display.set_caption('Snake')
pygame.display.flip()


#Step 4: Set up the game loop
while True:
    print("Snake events")
