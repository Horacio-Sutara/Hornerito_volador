import pygame
import Constantes as const
import Sonido
import Puntaje
import Objeto as obj
import random
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

        self.boton_sonido=Sonido.Sonido(const.boton_sonido)

    def mostrar(self):
        self.inicio=True
        while self.inicio:
            self.ventana.blit(self.fondo,(0,0))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.boton_inicio.es_click(evento):
                    self.boton_sonido.reproducir()
                    self.inicio=False
                    self.ejecutar=True
                if self.boton_salir.es_click(evento):
                    self.boton_sonido.reproducir()
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
        self.una_vez=True
        
        self.bloque=Arboles(
            [const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10,const.largo_pantalla-10],
            [210,180,150,120,90,60,30,0,const.ancho_pantalla-210,const.ancho_pantalla-180,const.ancho_pantalla-150,const.ancho_pantalla-120,const.ancho_pantalla-90,const.ancho_pantalla-60,const.ancho_pantalla-30,const.ancho_pantalla],self.pantalla,
            [const.imagen_arbol_ultra_superior,const.imagen_arbol_mega_superior,const.imagen_arbol_super_superior,const.imagen_arbol_alto_superior,const.imagen_arbol_medio_superior,const.imagen_arbol_bajo_superior,const.imagen_arbol_chato_superior,const.imagen_arbol_piso_superior,
             const.imagen_arbol_ultra_inferior,const.imagen_arbol_mega_inferior,const.imagen_arbol_super_inferior,const.imagen_arbol_alto_inferior,const.imagen_arbol_medio_inferior,const.imagen_arbol_bajo_inferior,const.imagen_arbol_chato_inferior,const.imagen_arbol_piso_inferior],
            const.Velocidad_personaje/2,16)
        self.band=False        
        self.fondo_sonido.reproducir()

        self.puntaje_sonido=Sonido.Sonido(const.puntaje_sonido)
        self.puntaje=Puntaje.Puntaje(posicion=(const.ancho_pantalla-150,10))

        self.muerte_sonido=Sonido.Sonido(const.muerte_sonido)
        self.muerte_sonido.ajustar_volumen(0.5)

        self.caer=True
        self.tiempo_colision=None

        self.game=False
        self.activar_menu=False
        self.cerrar=False

        self.numero_aleatorio_muro_superior = 0
        self.numero_aleatorio_muro_inferior = 8
        self.no_muro_superior=False
        self.no_muro_inferior=False
        self.desplazar_al_morir=True

    def menu(self, pantalla):
        self.fondo_sonido.reproducir()
        menu=Menu(pantalla,const.fondo_imagen,[const.jugar_imagen,const.jugar_imagen_ampliacion]
                  ,[const.salir_imagen,const.salir_imagen_ampliacion])
        menu.mostrar()
        self.game= menu.ejecutar
        self.cerrar=menu.salir

    def generar_numero(self):
        self.no_muro_superior=False
        self.no_muro_inferior=False
        self.numero_aleatorio_muro_superior=random.randint(0, 6)

        if self.numero_aleatorio_muro_superior==0:
            self.numero_aleatorio_muro_inferior=random.randint(14, 15)
        elif self.numero_aleatorio_muro_superior==1:
            self.numero_aleatorio_muro_inferior=random.randint(13, 14)
        elif self.numero_aleatorio_muro_superior==2:
            self.numero_aleatorio_muro_inferior=random.randint(12, 13)
        elif self.numero_aleatorio_muro_superior==3:
            self.numero_aleatorio_muro_inferior=random.randint(11, 12)
        elif self.numero_aleatorio_muro_superior==4:
            self.numero_aleatorio_muro_inferior=random.randint(10, 11)
        elif self.numero_aleatorio_muro_superior==5:
            self.numero_aleatorio_muro_inferior=random.randint(9, 10)
        else:
            self.numero_aleatorio_muro_inferior=random.randint(8, 9)

            
    def jugar(self):
        self.generar_numero()
        self.band=False
        self.bloque.reestablecer_posicion()
        self.caer=True
        self.puntaje.resetear()
        self.flappy.reestablecer()
        self.flappy.movimientos.aceleracion=0
        self.bloque.activar_obstaculo(self.numero_aleatorio_muro_superior)
        self.bloque.activar_obstaculo(self.numero_aleatorio_muro_inferior)
        self.flappy.originales_sprites()
        self.una_vez=True
        self.desplazar_al_morir=True
        while self.game:
            self.fondo_sonido.reproducir()
            self.reloj.tick(const.fps)
            self.pantalla.blit(self.fondo,(0,0))

            self.flappy.dibujar()

            if self.caer:
                self.flappy.caer()
            if self.band==False:
                self.flappy.actualizar_sprite()
                self.bloque.desplazar(self.numero_aleatorio_muro_inferior)
                if self.bloque.desplazar(self.numero_aleatorio_muro_superior):
                    self.bloque.desactivar_obstaculo(self.numero_aleatorio_muro_superior)
                    self.bloque.desactivar_obstaculo(self.numero_aleatorio_muro_inferior)
                    self.generar_numero()
                    self.bloque.activar_obstaculo(self.numero_aleatorio_muro_superior)
                    self.bloque.activar_obstaculo(self.numero_aleatorio_muro_inferior)
                
            else:
                if self.una_vez:
                    self.flappy.cambiar_sprites(const.imagenes_Hornero_colision)
                    self.una_vez=False
                if  self.flappy.movimientos.indice!=2:
                    self.flappy.actualizar_sprite(40)
                elif self.flappy.movimientos.indice==2 and self.desplazar_al_morir:
                    self.desplazar_al_morir=False
                    self.flappy.mover_abajo(10)
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
            
            if (const.Posicion_x-const.Ancho_personaje/2-5<self.bloque.lista_obstaculos[self.numero_aleatorio_muro_inferior].pos_x+100<const.Posicion_x-const.Ancho_personaje/2):
                self.puntaje_sonido.reproducir()
                self.puntaje.aumentar()

            if pygame.sprite.spritecollide(self.flappy.movimientos, self.bloque.personaje, False):
                self.muerte_sonido.reproducir()
                print("¡Colisión detectada con el obstáculo! ", self.flappy.movimientos.pos_x," ",self.bloque.lista_obstaculos[self.numero_aleatorio_muro_inferior].pos_x)
                self.tiempo_colision=pygame.time.get_ticks()
                self.flappy.movimientos.aceleracion=0
                if self.flappy.movimientos.rect.colliderect(self.bloque.lista_obstaculos[self.numero_aleatorio_muro_inferior]):
                    if (self.bloque.lista_obstaculos[self.numero_aleatorio_muro_inferior].pos_x<291):
                        self.caer=False
                        self.flappy.mover_arriba()

                        print("moviendo")
                    elif self.bloque.lista_obstaculos[self.numero_aleatorio_muro_inferior].pos_x>=291:
                        self.flappy.mover_izquierda()
                        print("desplazar")

                if self.flappy.movimientos.rect.colliderect(self.bloque.lista_obstaculos[self.numero_aleatorio_muro_superior]):
                    if self.bloque.lista_obstaculos[self.numero_aleatorio_muro_superior].pos_x>=291:
                        self.flappy.mover_izquierda()
                        print("desplazar")
                    else:
                        self.flappy.mover_abajo(10)
                self.band=True
            if self.tiempo_colision:
                self.tiempo_actual = pygame.time.get_ticks()
                # Si han pasado 5 segundos (5000 ms) desde la colisión
                if self.tiempo_actual - self.tiempo_colision >= 1600:
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
