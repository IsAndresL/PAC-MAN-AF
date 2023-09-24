import pygame
import sys

pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

# Colores
negro = (0, 0, 0)

# Pac-Man (imagen redimensionada)
pac_man_original = pygame.image.load("pac_man.png")
pac_man_tamano = (30, 30)  # Tamaño deseado
pac_man = pygame.transform.scale(pac_man_original, pac_man_tamano)
pac_man_rect = pac_man.get_rect()
pac_man_x = 400
pac_man_y = 300
velocidad = 1

# Laberinto
laberinto = pygame.image.load("laberinto.png")

# Loop del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover Pac-Man
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pac_man_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        pac_man_x += velocidad
    if teclas[pygame.K_UP]:
        pac_man_y -= velocidad
    if teclas[pygame.K_DOWN]:
        pac_man_y += velocidad

    # Limitar movimiento dentro del laberinto
    pac_man_rect.x = pac_man_x
    pac_man_rect.y = pac_man_y

    if pac_man_rect.left < 0:
        pac_man_x = 0
    if pac_man_rect.right > 800:
        pac_man_x = 800 - pac_man_rect.width
    if pac_man_rect.top < 0:
        pac_man_y = 0
    if pac_man_rect.bottom > 600:
        pac_man_y = 600 - pac_man_rect.height

    # Dibuja el fondo
    pantalla.fill(negro)

    # Dibuja el laberinto
    pantalla.blit(laberinto, (0, 0))

    # Dibuja Pac-Man
    pantalla.blit(pac_man, (pac_man_x, pac_man_y))

    pygame.display.flip()
