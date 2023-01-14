import pygame
from animation import *
from constants import *
import random
import time

pygame.init()


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desktop Buddy!")
WINDOW.fill(BLACK)
pygame.display.update()

imageTest = idleImages[0]
idleIndex = 0


run = True
while run:

    if idleIndex == 4:
        idleIndex = 0
    

    WINDOW.blit(idleImages[idleIndex], (-50, -50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0] == 1 and screenPressed == False:
            screenPressed = True
            randInt = random.choice([0,1])
            if randInt == 0:
                playBlockAnimation(WINDOW)
                screenPressed = False
            else:
                playAttackAnimation(WINDOW)
                screenPressed = False
    idleIndex  += 1
    time.sleep(0.15)


pygame.quit()
 