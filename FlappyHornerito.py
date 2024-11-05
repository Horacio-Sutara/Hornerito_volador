import pygame
from pygame.locals import *

pygame.init()

ancho_pantalla = 664
largo_pantalla = 736

pantalla = pygame.display.set_mode((ancho_pantalla, largo_pantalla)) #creamos la pantalla
pygame.display.set_caption('Flappy Hornerito')

run = True
#owo
#Imagenes cargadas
bg = pygame.image.load('bg.png')

while run: #ciclo de ejecucion del juego
    pantalla.blit(bg, (0,0)) #cargamos el fondo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() #actualiza todo lo que esta en pantalla

pygame.quit()