import pygame
import Constantes as const
import Personaje as pj
from pygame.locals import *

#limitador de fps (si se cambia se debe ajustar los parametros de velocidad y gravedad)
reloj = pygame.time.Clock()

pygame.init()

#creacion de pantalla y nombre
pantalla = pygame.display.set_mode((const.ancho_pantalla, const.largo_pantalla)) #creamos la pantalla
pygame.display.set_caption('Flappy Hornerito')

run = True

#Imagen de fondo
bg = pygame.image.load(const.fondo_imagen)

#Crear personaje
Hornerito_grupo = pygame.sprite.Group()#Maneja los sprte del pj
flappy= pj.Hornerito (const.Posicion_x,const.Posicion_y,pantalla) #crea al pj
Hornerito_grupo.add(flappy)# asigna los sprites al pj


while run: #ciclo de ejecucion del juego
    reloj.tick(const.fps)
    
    pantalla.blit(bg, (0,0)) #cargamos el fondo

    Hornerito_grupo.draw(pantalla)#dibuja al pj en la pantalla
    Hornerito_grupo.update()# cambia el sprite
    flappy.caer()# actua la gravedad en el pj

    for event in pygame.event.get():
        if event.type == pygame.QUIT:# comando para cerrar la pantalla
            run = False

        if event.type==pygame.KEYDOWN:# detecta la presion del teclado
            
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:#detecta w o space
                flappy.mover_arriba()# activa el salto

    pygame.display.update() #actualiza todo lo que esta en pantalla


pygame.quit()# Cierra el programa

