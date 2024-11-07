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

# imagenes (sprites)
jugar_imagen="boton-jugar.png"
jugar_imagen_ampliacion="boton-jugar1.png"

salir_imagen="boton-salir.png"
fondo_imagen='bg.png'
imagen_arbol_alto_superior=[pygame.image.load("alto-arriba.png")]
imagen_arbol_medio_superior=[pygame.image.load("medio-arriba.png")]
imagen_arbol_bajo_superior=[pygame.image.load("bajo-arriba.png")]
imagen_arbol_alto_inferior=[pygame.image.load("alto-abajo.png")]
imagen_arbol_medio_inferior=[pygame.image.load("medio-abajo.png")]
imagen_arbol_bajo_inferior=[pygame.image.load("bajo-abajo.png")]
imagenes_Hornero=[]
imagenes_Hornero_colision=[pygame.image.load("Hornerito-muerto1.png"),pygame.image.load("Hornerito-muerto2.png")]
for auxiliar in range (1,5):
            img = pygame.image.load(f"horneritoSprite{auxiliar}.png")
            imagenes_Hornero.append(img)
