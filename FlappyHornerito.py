import pygame
import Constantes as const
import Sonido
import Puntaje
import Objeto as obj

import sys

from Personaje import Personaje 
from Personaje import Arboles


class Menu():
    def __init__(self,ventana,fondo,imagen_boton1,imagen_boton2):
        self.ventana=ventana
        self.inicio=False
        self.ejecutar=False
        self.salir=False
        self.fondo=pygame.image.load(fondo)
        self.imagen_boton_normal = pygame.image.load(imagen_boton1[0]).convert_alpha()
        self.imagen_boton_hover = pygame.image.load(imagen_boton1[1]).convert_alpha()
        self.boton_inicio= obj.Boton(220, 100, self.imagen_boton_normal, self.imagen_boton_hover)
        #cerrar
        self.imagen_boton_normal= pygame.image.load(imagen_boton2[0]).convert_alpha()
        self.imagen_boton_hover= pygame.image.load(imagen_boton2[1]).convert_alpha()
        self.boton_salir=obj.Boton(220, 350, self.imagen_boton_normal, self.imagen_boton_hover)

    def mostrar(self):
        self.inicio=True
        while self.inicio:
            self.ventana.blit(self.fondo,(0,0))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.boton_inicio.es_click(evento):
                    self.inicio=False
                    self.ejecutar=True
                if self.boton_salir.es_click(evento):
                    self.inicio=False
                    self.ejecutar=False
                    self.salir=True
            self.boton_inicio.dibujar(self.ventana)
            self.boton_salir.dibujar(self.ventana)
            pygame.display.update()

class Juego():

    def __init__(self,fondo_sonido=const.fondo_sonido):
        pygame.init()
        self.pantalla = pygame.display.set_mode((const.ancho_pantalla, const.largo_pantalla)) #creamos la pantalla
        pygame.display.set_caption('Flappy Hornerito')
        self.fondo = pygame.image.load(const.fondo_imagen)
        self.reloj = pygame.time.Clock()
        self.fondo_sonido=Sonido.Sonido(fondo_sonido)
        self.flappy= Personaje(const.Posicion_x,const.Posicion_y,self.pantalla,const.imagenes_Hornero,const.Velocidad_personaje,const.Velocidad_personaje,const.gravedad)
        self.bloque=Arboles([const.largo_pantalla-10,const.largo_pantalla-10],[120,const.ancho_pantalla-120],self.pantalla,
                    [const.imagen_arbol_alto_superior,const.imagen_arbol_alto_inferior],const.Velocidad_personaje/2,2)
        self.band=False        
        self.fondo_sonido.reproducir()

        self.puntaje_sonido=Sonido.Sonido(const.puntaje_sonido)
        self.puntaje=Puntaje.Puntaje(posicion=(const.ancho_pantalla-150,10))

        self.caer=True
        self.tiempo_colision=None

        self.game=False
        self.activar_menu=False
        self.cerrar=False



    def menu(self, pantalla):
        self.fondo_sonido.reproducir()
        menu=Menu(pantalla,const.fondo_imagen,[const.jugar_imagen,const.jugar_imagen_ampliacion]
                  ,[const.salir_imagen,const.salir_imagen_ampliacion])
        menu.mostrar()
        self.game= menu.ejecutar
        self.cerrar=menu.salir

    def jugar(self):
        
        self.band=False
        self.bloque.reestablecer_posicion()
        self.caer=True
        self.puntaje.resetear()
        self.flappy.reestablecer()
        self.flappy.movimientos.aceleracion=0
        while self.game:
            self.fondo_sonido.reproducir()
            self.reloj.tick(const.fps)
            self.pantalla.blit(self.fondo,(0,0))

            self.flappy.dibujar()
            self.flappy.actualizar_sprite()

            if self.caer:
                self.flappy.caer()
            if self.band==False:
                self.bloque.desplazar(0)
                self.bloque.desplazar(1)
            self.bloque.dibujar()
            self.puntaje.dibujar(self.pantalla)
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    self.game=False
                    self.cerrar=True
                    pygame.quit()
                    sys.exit()
                
                if event.type== pygame.KEYDOWN:
                    if (event.key==pygame.K_w or event.key==pygame.K_SPACE) and self.band==False:
                        self.flappy.salto()
            
            if (const.Posicion_x-const.Ancho_personaje/2-5<self.bloque.lista_obstaculos[1].pos_x+100<const.Posicion_x-const.Ancho_personaje/2):
                self.puntaje_sonido.reproducir()
                self.puntaje.aumentar()
                self.puntaje_sonido.reproducir()

            if pygame.sprite.spritecollide(self.flappy.movimientos, self.bloque.personaje, False):
                print("¡Colisión detectada con el obstáculo! ", self.flappy.movimientos.pos_x," ",self.bloque.lista_obstaculos[1].pos_x)
                self.tiempo_colision=pygame.time.get_ticks()
                self.flappy.movimientos.aceleracion=0
                if self.flappy.movimientos.rect.colliderect(self.bloque.lista_obstaculos[1]):
                    if (self.bloque.lista_obstaculos[1].pos_x<291):
                        self.caer=False
                        self.flappy.mover_arriba()

                        print("moviendo")
                    elif self.bloque.lista_obstaculos[1].pos_x>=291:
                        self.flappy.mover_izquierda()
                        print("desplazar")

                if self.flappy.movimientos.rect.colliderect(self.bloque.lista_obstaculos[0]):
                    if self.bloque.lista_obstaculos[0].pos_x>=291:
                        self.flappy.mover_izquierda()
                        print("desplazar")
                self.band=True
            if self.tiempo_colision:
                self.tiempo_actual = pygame.time.get_ticks()

                if self.tiempo_actual - self.tiempo_colision >= 1000:
                    self.game=False
                    self.tiempo_colision = None  # Resetea el tiempo de colisión

            pygame.display.update() #actualiza todo lo que esta en pantalla


    def pantalla_final(self):
        menu=Menu(self.pantalla,const.fondo_perder,[const.retry_imagen,const.retry_imagen_ampliacion]
                  ,[const.ir_menu_imagen,const.ir_menu_imagen_ampliacion])
        menu.mostrar()
        self.game=menu.ejecutar
        self.activar_menu=menu.salir
        
    def ejecutar(self):
        self.menu(self.pantalla)
        while(not self.cerrar):
            if self.game:
                self.jugar()
            self.pantalla_final()
            if self.activar_menu:
                self.activar_menu=False
                self.menu(self.pantalla)







menu=Juego()
menu.ejecutar()

