import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((300, 300))
CLOCK = pygame.time.Clock()

# 시스템 글꼴에서 Font 객체를 만듦
sysfont  = pygame.font.SysFont(None, 36)
# 텍스트를 공백으로 초기화
txt = sysfont.render("0", True, (0, 0, 0))
# 숫자 초기화
n = 0

while True :
    SCREEN.fill((255, 255, 255))

    for event in pygame.event.get() :
        if event.type == QUIT or event.key == K_ESCAPE :
            pygame.quit()
            sys.exit()
        # 키보드가 눌리면 산술연산하는 하는 코드 작성
        # 키보드가 눌리면
        if event.type == KEYDOWN:
            # ↑ 키가 눌리면 + 10
            if event.key == K_UP :
                n += 10
            # ↓ 키가 눌리면 - 10
            if event.key == K_DOWN :
                n -= 10
            # ← 키가 눌리면 * 10
            if event.key == K_LEFT :
                n *= 10    
            # → 키가 눌리면 // 10
            if event.key == K_RIGHT :
                n //= 10
        # 왼쪽 마우스 클릭하면 0으로 초기화하기
        if event.type == MOUSEBUTTONDOWN :
            if event.button == 1 :
                n = 0
    txt = sysfont.render('%d' % n, True, (0, 0, 0))
    SCREEN.blit(txt, (100, 120))
    pygame.display.update()
    CLOCK.tick(60)
