import pygame
import Constantes as const

class Sonido:
    def __init__(self, archivo):
        # Inicializa el módulo de sonido si no está ya inicializado
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        # Carga el archivo de sonido
        self.sonido = pygame.mixer.Sound(archivo)
    
    def reproducir(self):
        """Reproduce el sonido"""
        self.sonido.play()
    
    def detener(self):
        """Detiene el sonido si está reproduciéndose"""
        self.sonido.stop()
    
    def ajustar_volumen(self, volumen):
        """Ajusta el volumen del sonido entre 0.0 y 1.0"""
        self.sonido.set_volume(volumen)

