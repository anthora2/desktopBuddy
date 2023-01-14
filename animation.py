import pygame
from constants import *
import time

def animate(window, image):
    window.fill(BLACK)
    window.blit(image, (-50, -50))

def playAttackAnimation(window):
    for image in attackImages:
        animate(window, image)
        pygame.display.update()
        time.sleep(0.1)


def playBlockAnimation(window):
    for image in blockImages:
        animate(window, image)
        pygame.display.update()
        time.sleep(0.1)