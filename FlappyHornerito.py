import pygame
import Constantes as const
import Personaje as pj
from pygame.locals import *

reloj = pygame.time.Clock()

pygame.init()


pantalla = pygame.display.set_mode((const.ancho_pantalla, const.largo_pantalla)) #creamos la pantalla
pygame.display.set_caption('Flappy Hornerito')

run = True

#Imagenes cargadas
bg = pygame.image.load(const.fondo_imagen)


Hornerito_grupo = pygame.sprite.Group()
flappy= pj.Hornerito (const.Posicion_x,const.Posicion_y,pantalla)
Hornerito_grupo.add(flappy)


while run: #ciclo de ejecucion del juego
    reloj.tick(const.fps)
    
    pantalla.blit(bg, (0,0)) #cargamos el fondo

    Hornerito_grupo.draw(pantalla)
    Hornerito_grupo.update()
    flappy.caer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type==pygame.KEYDOWN:
            
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                flappy.mover_arriba()

    pygame.display.update() #actualiza todo lo que esta en pantalla


pygame.quit()

