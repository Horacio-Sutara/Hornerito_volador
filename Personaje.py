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
    def __init__(self, x, y, interfaz, imagen_pj, velocidad, cantidad_obstaculos):
        self.personaje = pygame.sprite.Group()
        self.lista_obstaculos = []
        self.longitud = cantidad_obstaculos
        for i in range(cantidad_obstaculos):
            movimientos = Movimiento(x[i], y[i], interfaz, imagen_pj[i], velocidad)
            movimientos.visible = False  # Cada obstáculo comienza no visible
            self.personaje.add(movimientos)
            self.lista_obstaculos.append(movimientos)

    def numero_obstaculos(self):
        return self.longitud
    
    def dibujar(self):
        # Solo dibuja los obstáculos que están visibles
        for obstaculo in self.lista_obstaculos:
            if obstaculo.visible:
                self.personaje.draw(obstaculo.ventana)

    def actualizar_sprite(self):
        for obstaculo in self.lista_obstaculos:
            if obstaculo.visible:
                obstaculo.update()  # Cambia el sprite solo si es visible

    def desplazar(self, obstaculo_index):
        obstaculo = self.lista_obstaculos[obstaculo_index]
        reinicio=False
        if obstaculo.visible:  # Solo desplaza si el obstáculo es visible
            obstaculo.mover_izquierda()
            if -const.Ancho_personaje * 2 > obstaculo.pos_x:
                obstaculo.pos_x = obstaculo.largo_ventana + 100
                reinicio=True
            obstaculo.rect.center = (obstaculo.pos_x, obstaculo.pos_y)
            return reinicio


    def activar_obstaculo(self, obstaculo_index):
        """ Activa un obstáculo específico para que sea visible y se mueva """
        if 0 <= obstaculo_index < len(self.lista_obstaculos):
            self.lista_obstaculos[obstaculo_index].visible = True
    
    def desactivar_obstaculo(self, obstaculo_index):
        """ Desactiva un obstáculo específico para que deje de ser visible """
        if 0 <= obstaculo_index < len(self.lista_obstaculos):
            self.lista_obstaculos[obstaculo_index].visible = False

    def reestablecer_posicion(self):
        for obstaculo in self.lista_obstaculos:
            obstaculo.pos_x = obstaculo.largo_ventana + 100
            obstaculo.visible = False  # Al reestablecer, desactiva todos
            obstaculo.rect.center = (obstaculo.pos_x, obstaculo.pos_y)