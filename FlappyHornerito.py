import pygame
from pygame.locals import *

#inicio owo

pygame.init()

ancho_pantalla = 664
largo_pantalla = 736

pantalla = pygame.display.set_mode((ancho_pantalla, largo_pantalla)) #creamos la pantalla
pygame.display.set_caption('Flappy Hornerito')

run = True

#Imagenes cargadas
bg = pygame.image.load('bg.png')

#clase del hornerito


class Hornerito(pygame.sprite.Sprite)
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__ (self)
        self.image=pygame.image.load("")
        self.rect= self.image.get_rect ()
        self.rect.center =[x, y]

Hornerito_grupo = pygame.sprite.Group()
flappy= Hornerito (100,int(largo_pantalla/2))
Hornerito_grupo.add(flappy)

pygame.quit()

while run: #ciclo de ejecucion del juego
    pantalla.blit(bg, (0,0)) #cargamos el fondo

    Hornerito_grupo.draw(pantalla)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() #actualiza todo lo que esta en pantalla


