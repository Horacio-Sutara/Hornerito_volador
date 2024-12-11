import pygame

class Puntaje:
    def __init__(self, fuente=36, color=(0, 0, 0), posicion=(10, 10)):
        # Inicializar el puntaje, la fuente y otros atributos
        self.puntaje = 0
        self.color = color
        self.posicion = posicion
        self.fuente = pygame.font.Font(None, fuente)  # Puedes cambiar None por una ruta de fuente específica
    
    def aumentar(self, cantidad=1):
        """Aumenta el puntaje en una cantidad dada (por defecto, 1)"""
        self.puntaje += cantidad
    
    def resetear(self):
        """Reinicia el puntaje a 0"""
        self.puntaje = 0
    
    def dibujar(self, pantalla):
        """Renderiza el puntaje en la pantalla"""
        texto_puntaje = self.fuente.render(f"Puntaje: {self.puntaje}", True, self.color)
        pantalla.blit(texto_puntaje, self.posicion)
