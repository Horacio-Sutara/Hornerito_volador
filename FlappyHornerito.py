import pygame
import Constantes as const
import Personaje as pj
import Sonido
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
flappy= pj.Hornerito (const.Posicion_x,const.Posicion_y,pantalla,imagen_pj=const.imagenes_Hornero) #crea al pj
Hornerito_grupo.add(flappy)# asigna los sprites al pj
muro_superior=pj.Hornerito(const.largo_pantalla-10, 120,pantalla,const.imagen_arbol_alto_superior)
muro_inferior=pj.Hornerito(const.largo_pantalla-10, const.ancho_pantalla-120,pantalla,const.imagen_arbol_alto_inferior)
obstaculos = pygame.sprite.Group()
obstaculos.add(muro_superior)
obstaculos.add(muro_inferior)
band=False

#crear clase sonido puntaje
puntaje_sonido=Sonido.Sonido(const.puntaje_sonido)

while run: #ciclo de ejecucion del juego
    reloj.tick(const.fps)
    
    pantalla.blit(bg, (0,0)) #cargamos el fondo

    Hornerito_grupo.draw(pantalla)#dibuja al pj en la pantalla
    Hornerito_grupo.update()# cambia el sprite
    flappy.caer()# actua la gravedad en el pj
    if band==False:
        muro_superior.mover_izquierda()
        muro_inferior.mover_izquierda()
    obstaculos.draw(pantalla)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# comando para cerrar la pantalla
            run = False

        if event.type==pygame.KEYDOWN:# detecta la presion del teclado
            
            if (event.key == pygame.K_w or event.key == pygame.K_SPACE) and band==False:#detecta w o space
                flappy.mover_arriba()# activa el salto
    if muro_inferior.pos_x<const.Posicion_x-const.Ancho_personaje:
        puntaje_sonido.reproducir()

    if pygame.sprite.spritecollide(flappy, obstaculos, False):
        print("¡Colisión detectada con el obstáculo! ", flappy.pos_x," ",muro_inferior.pos_x)
        band=True

    pygame.display.update() #actualiza todo lo que esta en pantalla


pygame.quit()# Cierra el programa

