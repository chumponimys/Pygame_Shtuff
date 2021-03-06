import pygame
from pygame.locals import *
import sys
from OpenGLLibrary import *

pygame.init()

Screen = (800,600)
Window = glLibWindow(Screen,caption="Objects Test")
View3D = glLibView3D((0,0,Screen[0],Screen[1]),45)
View3D.set_view() 

drawing = 0
#Objects = [glLibObjFromFile("ExamplesData/test1.obj")]
Objects = [glLibObjCube(),
           glLibObjTeapot(),
           glLibObjSphere(64),
           glLibObjCylinder(0.5,1.0,64),
           glLibObjCone(0.5,1.8,64),
           glLibObjFromFile("ExamplesData/UberBall.obj"),
           glLibObjFromFile("ExamplesData/test1.obj")]
yrot = 0
xrot = 0
while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_RETURN:
                drawing += 1
                if drawing == 6:
                    drawing = 0
            
    Window.clear()
    Objects[drawing].draw([0,-0.5,-6],[[0,yrot,0],[xrot,0,0]])
    Window.flip()

    yrot += .25
    yrot = yrot % 360
    xrot += 0.1
    xrot = xrot % 360
