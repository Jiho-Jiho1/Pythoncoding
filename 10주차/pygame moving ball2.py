import sys, pygame
from pygame.locals import *

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Pygame bouncing ball game")

pygame.key.set_repeat(5,5)

Tick = pygame.time.Clock()

x, y = 300, 10
v = 0
g = 0.5

BALLimage = pygame.image.load("ball.png")
BALLimage = pygame.transform.scale(BALLimage, (100, 100))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x += 5
            elif event.key == K_LEFT:
                x -= 5
            elif event.key == K_SPACE:
                v = -10
    screen.fill((0, 0, 0))
    v += g
    y += v

    if y >= h - 100:
        y = h - 100
        v = - v
    
    if x <= 0:
        x = 0
    if x >= w -100:
        x = w - 100

    screen.blit(BALLimage, (x, y))
    pygame.display.update()
    
    Tick.tick(60)