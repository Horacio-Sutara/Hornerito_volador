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
    def __init__(self, x, y,interfaz):
        self.ventana=interfaz
        self.largo_ventana,self.alto_ventana=interfaz.get_size()
        self.pos_x=x
        self.pos_y=y

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
    

    def mover_abajo(self,velocidad=const.Velocidad_personaje):
        self.pos_y+=velocidad
        if self.alto_ventana<self.pos_y+const.Alto_personaje/2:
            self.pos_y=self.alto_ventana-const.Alto_personaje/2
        self.rect.center=[self.pos_x,self.pos_y]

    def caer(self):
        self.mover_abajo(3)

Hornerito_grupo = pygame.sprite.Group()
flappy= Hornerito (100,int(const.largo_pantalla/2),pantalla)
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

    pygame.display.update() #actualiza todo lo que esta en pantalla


pygame.quit()

