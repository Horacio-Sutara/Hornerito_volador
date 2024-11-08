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
puntaje_sonido="puntaje.wav"
fondo_sonido="fondo.wav"
muerte_sonido="muerte.wav"
boton_sonido="boton.wav"


# imagenes (sprites)
jugar_imagen="boton-jugar.png"
jugar_imagen_ampliacion="boton-jugar1.png"

salir_imagen="boton-salir.png"
salir_imagen_ampliacion="boton-salir1.png"

fondo_imagen='bg.png'
fondo_perder="fondo-muerte.png"

retry_imagen="Volver-a-jugar.png"
retry_imagen_ampliacion="Volver-a-jugar1.png"

ir_menu_imagen="Volver-al-menu.png"
ir_menu_imagen_ampliacion="Volver-al-menu1.png"

imagen_arbol_ultra_superior=[pygame.image.load("ultra-arriba.png")]
imagen_arbol_mega_superior=[pygame.image.load("mega-arriba.png")]
imagen_arbol_super_superior=[pygame.image.load("super-arriba.png")]
imagen_arbol_alto_superior=[pygame.image.load("alto-arriba.png")]
imagen_arbol_medio_superior=[pygame.image.load("medio-arriba.png")]
imagen_arbol_bajo_superior=[pygame.image.load("bajo-arriba.png")]
imagen_arbol_chato_superior=[pygame.image.load("chato-arriba.png")]
imagen_arbol_piso_superior=[pygame.image.load("piso-arriba.png")]

imagen_arbol_ultra_inferior=[pygame.image.load("ultra-abajo.png")]
imagen_arbol_mega_inferior=[pygame.image.load("mega-abajo.png")]
imagen_arbol_super_inferior=[pygame.image.load("super-abajo.png")]
imagen_arbol_alto_inferior=[pygame.image.load("alto-abajo.png")]
imagen_arbol_medio_inferior=[pygame.image.load("medio-abajo.png")]
imagen_arbol_bajo_inferior=[pygame.image.load("bajo-abajo.png")]
imagen_arbol_chato_inferior=[pygame.image.load("chato-abajo.png")]
imagen_arbol_piso_inferior=[pygame.image.load("piso-abajo.png")]

imagenes_Hornero=[]
imagenes_Hornero_colision=[pygame.image.load("Hornerito-muerto1.png"),pygame.image.load("Hornerito-muerto2.png"),pygame.image.load("Hornerito-muerto3.png")]
for auxiliar in range (1,5):
            img = pygame.image.load(f"horneritoSprite{auxiliar}.png")
            imagenes_Hornero.append(img)
