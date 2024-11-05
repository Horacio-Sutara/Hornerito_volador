import pygame
import Constantes as const
from pygame.locals import *

reloj = pygame.time.Clock()

pygame.init()


pantalla = pygame.display.set_mode((const.ancho_pantalla, const.largo_pantalla)) #creamos la pantalla
pygame.display.set_caption('Flappy Hornerito')

run = True

#Imagenes cargadas
bg = pygame.image.load('bg.png')

#clase del hornerito


class Hornerito(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__ (self)
        self.imagenes= [ ]
        self.indice =0
        self.contador =0
        for auxiliar in range (1,5):
            img = pygame.image.load(f"horneritoSprite{auxiliar}.png")
            self.imagenes.append(img)
        self.image= self.imagenes[self.indice]
        self.rect= self.image.get_rect ()
        self.rect.center =[x, y]

        #esta parte es para actualizar el sprite

        def update(self):
            self.contador+=1
            cooldown= 4
            if self.contador > cooldown:
                self.contador=0
                self.indice+=1
                if self.indice >= len(self.imagenes):
                    self.indice= 0
            self.image=self.imagenes[self.indice]


Hornerito_grupo = pygame.sprite.Group()
flappy= Hornerito (100,int(const.largo_pantalla/2))
Hornerito_grupo.add(flappy)


while run: #ciclo de ejecucion del juego
    reloj.tick(const.fps)
    
    pantalla.blit(bg, (0,0)) #cargamos el fondo

    Hornerito_grupo.draw(pantalla)
    Hornerito_grupo.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() #actualiza todo lo que esta en pantalla


pygame.quit()

