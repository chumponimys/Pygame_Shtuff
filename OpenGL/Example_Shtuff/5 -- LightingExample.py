import pygame
from pygame.locals import *
import sys
from OpenGLLibrary import *

pygame.init()

Screen = (800,600)
Window = glLibWindow(Screen,caption="Lighting Test")
View3D = glLibView3D((0,0,Screen[0],Screen[1]),45)
View3D.set_view()

Camera = glLibCamera([0,0.5,6],[0,0,0])

glLibLighting(True)
Sun = glLibLight([0,100,0],Camera)
Sun.enable()

glLibColorMaterial(True) 

drawing = 0
Objects = [glLibObjCube(),glLibObjTeapot(),glLibObjSphere(64),glLibObjCylinder(0.5,1.0,64),glLibObjCone(0.5,1.8,64)]#,glLibObjFromFile("ExamplesData\UberBall.obj")]

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
                drawing = drawing % 5
            if event.key == K_1: glLibColor((255,255,255))
            if event.key == K_2: glLibColor((255,0,0))
            if event.key == K_3: glLibColor((255,128,0))
            if event.key == K_4: glLibColor((255,255,0))
            if event.key == K_5: glLibColor((0,255,0))
            if event.key == K_6: glLibColor((0,0,255))
            if event.key == K_7: glLibColor((128,0,255))
    if   key[K_LEFT]: Camera.set_target_pos([-6,0.5,0])
    elif key[K_RIGHT]: Camera.set_target_pos([6,0.5,0])
    elif key[K_UP]: Camera.set_target_pos([0,6,2])
    elif key[K_DOWN]: Camera.set_target_pos([0,-6,2])
    else: Camera.set_target_pos([0,0.5,6])

    Camera.update()
            
    Window.clear()
    Camera.set_camera()
    Sun.draw()
    Objects[drawing].draw()
    Window.flip()
