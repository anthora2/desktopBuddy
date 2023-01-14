import os
import pygame

WIDTH = 100
HEIGHT = 75


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screenPressed = False



realPath =  os.path.dirname(os.path.realpath(__file__))
def loadImage(imageName):
    image = pygame.image.load(os.path.join(realPath, 'images', imageName))
    return pygame.transform.scale(image, (200, 200))



#### IMAGES ####

attackImages = [
    loadImage('attack1.png'),
    loadImage('attack2.png'),
    loadImage('attack3.png'),
    loadImage('attack4.png'),
    loadImage('attack5.png'),
    loadImage('attack6.png'),
    loadImage('attack7.png'),
    loadImage('attack8.png'),
    loadImage('attack9.png'),
    loadImage('attack10.png'),
    loadImage('attack11.png'),
    loadImage('attack12.png'),
    loadImage('attack13.png'),
    loadImage('attack14.png'),
    loadImage('attack15.png'),
    loadImage('attack16.png'),
    loadImage('attack17.png')
]

blockImages = [
    loadImage('block1.png'),
    loadImage('block2.png'),
    loadImage('block3.png'),
    loadImage('block4.png'),
    loadImage('block5.png'),
    loadImage('block6.png'),
    loadImage('block7.png'),
    loadImage('block8.png'),
    loadImage('block9.png'),
    loadImage('block10.png'),
    loadImage('block11.png'),
    loadImage('block12.png'),
    loadImage('block13.png')

]

idleImages = [
    loadImage('idle1.png'),
    loadImage('idle2.png'),
    loadImage('idle3.png'),
    loadImage('idle4.png'),
]

deathImages = [
    loadImage('death1.png'),
    loadImage('death2.png'),
    loadImage('death3.png'),
    loadImage('death4.png'),
    loadImage('death5.png'),
    loadImage('death6.png'),
    loadImage('death7.png'),
    loadImage('death8.png'),
    loadImage('death9.png'),
    loadImage('death10.png'),
    loadImage('death11.png'),
    loadImage('death12.png')
]