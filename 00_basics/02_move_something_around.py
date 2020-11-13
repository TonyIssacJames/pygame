import pygame, sys, os
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#global variables
catx = 10
caty = 10
screen = None


#=========== Helper Functions ===================================
def quit_game():
    pygame.quit()
    sys.exit()

def process_input(events):
    global catx, caty, screen

    for event in events:
        print(event)
        if event.type == QUIT:
            quit_game()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game()
                elif event.key == K_LEFT:
                    catx -= 5
                    print("Move Left: ", catx)
                elif event.key == K_RIGHT:
                    catx += 5
                    print("Move Right: ", catx)
                else:
                    print("Unkonwn Key: ",event.key)

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (catx, 50, 50, 10))
    pygame.display.update()# update and rendder
    


#=================================================================
#Step 1: Initialize the Game
pygame.init()

#Step 2: Setup the Window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#Step 3: Setup the Surface
screen = pygame.display.get_surface()
screen.fill(BLACK)
pygame.display.set_caption('Snake')
pygame.display.flip()
pygame.display.update() #update the screen

#Step 4: Set up the game loop
while True:
    process_input(pygame.event.get())
            
