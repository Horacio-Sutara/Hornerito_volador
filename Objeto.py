import pygame
import Constantes as const
class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y,interfaz,imagen_pj):
        self.ventana=interfaz # asigna ventana a la que pertenece
        self.largo_ventana,self.alto_ventana=interfaz.get_size() #dimensiones de la ventana
        self.pos_x=x #posicion de inicio en x
        self.pos_y=y #posicion de inicio en y


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