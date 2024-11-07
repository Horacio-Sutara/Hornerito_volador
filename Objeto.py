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

class Movimiento(Objeto):
    def __init__(self, x, y,interfaz,imagen_pj,velocidad):

        super().__init__(x, y,interfaz,imagen_pj)
        self.velocidad=velocidad # velocidad 
    
    def mover_derecha(self,velocidad=None):
        if velocidad is None:
            self.pos_x-=self.velocidad
        else:
            self.pos_x-=velocidad
        self.rect.center=(self.pos_x,self.pos_y)
    
    def mover_izquierda(self,velocidad=None):
        if velocidad is None:
            self.pos_x+=self.velocidad
        else:
            self.pos_x+=velocidad
        self.rect.center=(self.pos_x,self.pos_y)

    def mover_abajo(self,velocidad=None):
        if velocidad is None:
            self.pos_y+=self.velocidad
        else:
            self.pos_y+=velocidad
        self.rect.center=(self.pos_x,self.pos_y)

    def mover_arriba(self,velocidad=None):# funcion de mover hacia abajo
        if velocidad is None:
            self.pos_y+=self.velocidad #traslacion hacia abajo
        else:
            self.pos_y+=velocidad
        self.rect.center=(self.pos_x,self.pos_y)# nueva posicion

class Gravedad(Movimiento):

    def __init__(self, x, y, interfaz, imagen_pj, velocidad,impulso, gravedad):
        super().__init__(x, y, interfaz, imagen_pj, velocidad)
        self.gravedad=gravedad
        self.aceleracion=0
        self.impulso=impulso


    def salto(self): # funcion del salto del pajaro
        if self.aceleracion<0:
            self.aceleracion+=-5
        else:
            self.aceleracion+=self.impulso #impulso inicial
        self.mover_arriba((self.aceleracion)*(-1))

    def caer(self):
        self.aceleracion+=self.gravedad # gravedad del personaje
        self.mover_abajo((self.aceleracion))
    
class Mostrar_Personaje():
    def __init__(self, x, y, interfaz, imagen_pj, velocidad, impulso, gravedad):
        self.movimientos=Gravedad(x, y, interfaz, imagen_pj, velocidad, impulso, gravedad)
        self.personaje=pygame.sprite.Group()
        self.personaje.add(self.movimientos)
    
    def dibujar(self):
        self.personaje.draw(self.movimientos.ventana)#dibuja al pj en la pantalla
    
    def actualizar_sprite(self):
        self.personaje.update()# cambia el sprite
class Boton:
    def __init__(self, x, y, imagen_normal, imagen_hover):
        # Carga las imágenes para el estado normal y el estado "hover"
        self.pos_x_normal=x
        self.pos_y_normal=y
        self.imagen_normal = imagen_normal
        self.imagen_hover = imagen_hover
        self.imagen_actual = self.imagen_normal  # Imagen que se muestra actualmente
        self.rect = self.imagen_normal.get_rect()
        self.rect.topleft = (x, y)
        self.click = False  # Para verificar si se ha hecho clic

    def dibujar(self, ventana):
        # Cambia la imagen actual según la posición del mouse
        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.imagen_actual = self.imagen_hover
            self.rect.topleft = (self.pos_x_normal-5, self.pos_y_normal)
        else:
            self.imagen_actual = self.imagen_normal
            self.rect.topleft = (self.pos_x_normal, self.pos_y_normal)

        # Dibuja la imagen actual en la ventana
        ventana.blit(self.imagen_actual, (self.rect.x, self.rect.y))

    def es_click(self, evento):
        # Comprueba si el botón ha sido clickeado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.click = True  # Registra el clic

        if evento.type == pygame.MOUSEBUTTONUP:
            if self.click and self.rect.collidepoint(evento.pos):
                self.click = False
                return True  # Retorna True si se ha hecho clic correctamente
        return False


