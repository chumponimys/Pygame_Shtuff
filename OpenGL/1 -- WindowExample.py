import pygame
from pygame.locals import *
import sys
from OpenGLLibrary import *

pygame.init()

Window = glLibWindow((800,600),caption="Window Test")
View = glLibView3D((0,0,800,600),45)
View.set_view()


while True:
    test_img = pygame.image.load("Piece_15.png")
    Window.blit(test_img, (100, 100))
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or key[K_ESCAPE]:
            sys.exit()
    Window.clear()
    Window.flip()
