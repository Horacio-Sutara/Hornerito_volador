import pygame
import Constantes as const
class Hornerito(pygame.sprite.Sprite):
    def __init__(self, x, y,interfaz,imagen_pj):
        self.ventana=interfaz # asigna ventana a la que pertenece
        self.largo_ventana,self.alto_ventana=interfaz.get_size() #dimensiones de la ventana
        self.pos_x=x #posicion de inicio en x
        self.pos_y=y #posicion de inicio en y

        self.velocidad=0 # velocidad inicial del pj (estatico)

        pygame.sprite.Sprite. __init__ (self)
        self.indice =0
        self.contador =0

        self.image= imagen_pj[self.indice]
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
    
    def mover_izquierda(self,velocidad=const.Velocidad_personaje):
        self.pos_x+=velocidad/2

        if -const.Ancho_personaje*2>self.pos_x:
            self.pos_x=self.largo_ventana-const.Ancho_personaje/2

        self.rect.center=(self.pos_x,self.pos_y)

    def mover_arriba(self,velocidad=const.Velocidad_personaje): # funcion del salto del pajaro
        if self.velocidad<0:
            velocidad=-5
        self.velocidad+=velocidad #impulso inicial
        self.pos_y-=velocidad # traslacion en eje y
        if const.Alto_personaje/2>self.pos_y: # limita los bordes de la pantalla
            self.pos_y=const.Alto_personaje/2
        self.rect.center=(self.pos_x,self.pos_y) #nueva posicion

    def mover_abajo(self,velocidad=const.Velocidad_personaje):# funcion de mover hacia abajo
        self.pos_y+=velocidad #traslacion hacia abajo
        if self.alto_ventana<self.pos_y-4:# limita borde inferior
            self.pos_y=self.alto_ventana-7
            self.velocidad=0
            
        elif const.Alto_personaje/2>self.pos_y:# limita borde superior 
            self.pos_y=const.Alto_personaje/2+1
            self.velocidad=0
        self.rect.center=(self.pos_x,self.pos_y)# nueva posicion

    def caer(self):
        self.velocidad+=const.gravedad # gravedad del personaje
        self.mover_abajo(self.velocidad)