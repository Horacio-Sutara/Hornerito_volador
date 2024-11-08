import pygame
import Constantes as const
from Objeto import Mostrar_Personaje
from Objeto import Movimiento
class Personaje(Mostrar_Personaje):
    def __init__(self, x, y, interfaz, imagen_pj, velocidad, impulso, gravedad):
        super().__init__(x, y, interfaz, imagen_pj, velocidad, impulso, gravedad)
        self.pos_inicial_x=x
        self.pos_inicial_y=y

    def salto(self):
        self.movimientos.salto() 
        if const.Alto_personaje/2>self.movimientos.pos_y: # limita los bordes de la pantalla
            self.movimientos.pos_y=const.Alto_personaje/2
            self.movimientos.rect.center=(self.movimientos.pos_x,self.movimientos.pos_y)# nueva posicion
            
    def caer(self):
        self.movimientos.caer()
        if self.movimientos.alto_ventana-30<self.movimientos.pos_y:# limita borde inferior
            self.movimientos.pos_y=self.movimientos.alto_ventana-31
            self.movimientos.aceleracion=0
            self.movimientos.rect.center=(self.movimientos.pos_x,self.movimientos.pos_y)# nueva posicion
        elif const.Alto_personaje/2>self.movimientos.pos_y:# limita borde superior 
            self.movimientos.pos_y=const.Alto_personaje/2+1
            self.movimientos.aceleracion=0
            self.movimientos.rect.center=(self.movimientos.pos_x,self.movimientos.pos_y)# nueva posicion
    def mover_izquierda(self):
        self.movimientos.mover_izquierda()
    def mover_arriba(self):
        self.movimientos.mover_arriba()
    def reestablecer(self):
        self.movimientos.pos_x=self.pos_inicial_x
        self.movimientos.pos_y=self.pos_inicial_y
        self.movimientos.posicionar(self.pos_inicial_x,self.pos_inicial_y)
    
class Arboles():

    def __init__(self, x, y, interfaz, imagen_pj, velocidad,cantidad_obstaculos):
        self.personaje=pygame.sprite.Group()
        self.lista_obstaculos=[]
        self.longitud=cantidad_obstaculos
        for i in range (cantidad_obstaculos):
            movimientos=Movimiento(x[i], y[i], interfaz, imagen_pj[i], velocidad)
            self.personaje.add(movimientos)
            self.lista_obstaculos.append(movimientos)

    def numero_obstaculos(self):
        return self.longitud
    def dibujar(self):
        self.personaje.draw(self.lista_obstaculos[0].ventana)#dibuja al pj en la pantalla
    
    def actualizar_sprite(self):
        self.personaje.update()# cambia el sprite

    def desplazar(self,obstaculo):
        self.lista_obstaculos[obstaculo].mover_izquierda()
        if -const.Ancho_personaje*2>self.lista_obstaculos[obstaculo].pos_x:
            self.lista_obstaculos[obstaculo].pos_x=self.lista_obstaculos[obstaculo].largo_ventana+100
        self.lista_obstaculos[obstaculo].rect.center=(self.lista_obstaculos[obstaculo].pos_x,self.lista_obstaculos[obstaculo].pos_y)
    def reestablecer_posicion(self):
        for i in range(self.longitud):
            self.lista_obstaculos[i].pos_x=self.lista_obstaculos[i].largo_ventana+100
            self.lista_obstaculos[i].rect.center=(self.lista_obstaculos[i].pos_x,self.lista_obstaculos[i].pos_y)