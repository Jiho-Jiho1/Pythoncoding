import pygame, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Jumping dino')
w = 800
h = 400
 
 
# set screen, fps
screen = pygame.display.set_mode((w, h))
Tick = pygame.time.Clock()