import pygame
import Constantes as const
class Hornerito(pygame.sprite.Sprite):
    def __init__(self, x, y,interfaz):
        self.ventana=interfaz
        self.largo_ventana,self.alto_ventana=interfaz.get_size()
        self.pos_x=x
        self.pos_y=y

        self.velocidad=0

        pygame.sprite.Sprite. __init__ (self)
        self.indice =0
        self.contador =0

        self.image= const.imagenes_Hornero[self.indice]
        self.rect= self.image.get_rect ()
        self.rect.center =[x, y]

        #esta parte es para actualizar el sprite

    def update(self,cooldown=const.cooldown):
            self.contador+=1
            if self.contador > cooldown:
                self.contador=0
                self.indice+=1
                if self.indice >= len(const.imagenes_Hornero):
                    self.indice= 0
            self.image=const.imagenes_Hornero[self.indice]
    
    def mover_arriba(self,velocidad=const.Velocidad_personaje):
        self.velocidad=velocidad
        self.pos_y-=velocidad
        if const.Alto_personaje/2>self.pos_y:
            self.pos_y=const.Alto_personaje/2
        self.rect.center=(self.pos_x,self.pos_y)

    def mover_abajo(self,velocidad=const.Velocidad_personaje):
        self.pos_y+=velocidad
        if self.alto_ventana<self.pos_y:
            self.pos_y=self.alto_ventana-1
            
        elif const.Alto_personaje/2>self.pos_y:
            self.pos_y=const.Alto_personaje/2+1
            self.velocidad=0
        self.rect.center=(self.pos_x,self.pos_y)

    def caer(self):
        self.velocidad+=const.gravedad
        self.mover_abajo(self.velocidad)