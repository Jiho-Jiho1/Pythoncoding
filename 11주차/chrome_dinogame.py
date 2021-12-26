import sys, pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400
 
 
# set screen, fps
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
fps = pygame.time.Clock()

# dino
imgDino1 = pygame.image.load('./dino1.png')
imgDino2 = pygame.image.load('./dino2.png')
dino_height = imgDino1.get_size()[1]
dino_bottom = MAX_HEIGHT - dino_height
dino_x = 50
dino_y = dino_bottom
jump_top = 200
leg_swap = True
is_bottom = True
is_go_up = False

# tree
imgTree = pygame.image.load('./tree.png')
tree_height = imgTree.get_size()[1]
tree_x = MAX_WIDTH
tree_y = MAX_HEIGHT - tree_height

while True:
    screen.fill((200, 200, 200))

    # event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if is_bottom:#Able to jump ONLY when touching floor
                is_go_up = True
                is_bottom = False
    #Dino move        
    if is_go_up:
        dino_y -= 10#Going up
    elif not is_go_up and not is_bottom:
        dino_y += 10#Going down
    #Dino top and bottom check
    if is_go_up and dino_y <= jump_top:
        is_go_up = False

    if not is_bottom and dino_y >= dino_bottom:
        is_bottom = True
        dino_y = dino_bottom
    
    #draw dino
    if leg_swap:
        screen.blit(imgDino1, (dino_x, dino_y))
        leg_swap = False
    
    else:
        screen.blit(imgDino2, (dino_x, dino_y))
        leg_swap = True
     
    #tree_move
    tree_x -= 20
    if tree_x <= 0:
        tree_x = MAX_WIDTH
    
    screen.blit(imgTree, (tree_x, tree_y))

    if tree_x - 30.0 <= dino_x <= tree_x + 30.0 and tree_y - 30.0 <= dino_y <= tree_y + 30.0:
        print("                                                You Lose! Game Over.")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fps.tick(30)
