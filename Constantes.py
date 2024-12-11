import pygame
ancho_pantalla = 640
largo_pantalla = 640
fps = 60
Alto_personaje=75
Ancho_personaje=60
Color_personaje=(23,255,0)
Velocidad_personaje=-8
Posicion_x=200
Posicion_y=int(largo_pantalla/2)
run = True


gravedad=0.2
cooldown= 4

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (100, 149, 237)
ROJO = (255,0,0)


# sonido
puntaje_sonido="Sound//puntaje.wav"
fondo_sonido="Sound//fondo.wav"
muerte_sonido="Sound//muerte.wav"
boton_sonido="Sound//boton.wav"


# imagenes (sprites)
jugar_imagen="image//boton-jugar.png"
jugar_imagen_ampliacion="image//boton-jugar1.png"

salir_imagen="image//boton-salir.png"
salir_imagen_ampliacion="image//boton-salir1.png"

fondo_imagen='image//bg.png'
fondo_perder="image//fondo-muerte.png"

retry_imagen="image//Volver-a-jugar.png"
retry_imagen_ampliacion="image//Volver-a-jugar1.png"

ir_menu_imagen="image//Volver-al-menu.png"
ir_menu_imagen_ampliacion="image//Volver-al-menu1.png"

imagen_arbol_ultra_superior=[pygame.image.load("image//ultra-arriba.png")]
imagen_arbol_mega_superior=[pygame.image.load("image//mega-arriba.png")]
imagen_arbol_super_superior=[pygame.image.load("image//super-arriba.png")]
imagen_arbol_alto_superior=[pygame.image.load("image//alto-arriba.png")]
imagen_arbol_medio_superior=[pygame.image.load("image//medio-arriba.png")]
imagen_arbol_bajo_superior=[pygame.image.load("image//bajo-arriba.png")]
imagen_arbol_chato_superior=[pygame.image.load("image//chato-arriba.png")]
imagen_arbol_piso_superior=[pygame.image.load("image//piso-arriba.png")]

imagen_arbol_ultra_inferior=[pygame.image.load("image//ultra-abajo.png")]
imagen_arbol_mega_inferior=[pygame.image.load("image//mega-abajo.png")]
imagen_arbol_super_inferior=[pygame.image.load("image//super-abajo.png")]
imagen_arbol_alto_inferior=[pygame.image.load("image//alto-abajo.png")]
imagen_arbol_medio_inferior=[pygame.image.load("image//medio-abajo.png")]
imagen_arbol_bajo_inferior=[pygame.image.load("image//bajo-abajo.png")]
imagen_arbol_chato_inferior=[pygame.image.load("image//chato-abajo.png")]
imagen_arbol_piso_inferior=[pygame.image.load("image//piso-abajo.png")]

imagenes_Hornero=[]
imagenes_Hornero_colision=[pygame.image.load("image//Hornerito-muerto1.png"),pygame.image.load("image//Hornerito-muerto2.png"),pygame.image.load("image//Hornerito-muerto3.png")]
for auxiliar in range (1,5):
            img = pygame.image.load(f"image//horneritoSprite{auxiliar}.png")
            imagenes_Hornero.append(img)
