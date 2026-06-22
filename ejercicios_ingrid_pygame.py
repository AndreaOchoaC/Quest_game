import pygame

#Inicializar Pygame
pygame.init()

# Crear y configurar pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Juego con Pygame")

# Ciclo de juego
running = True
# ----- VERSION 1: DIBUJAR UN RECTÁNGULO Y UN CÍRCULO -----
'''while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar la pantalla con un color
    screen.fill("#296014")  # Blanco

    # Dibujar objetos
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))  # Un rectángulo rojo
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 60)  # Un círculo azul

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()'''

# ----- VERSION 2: MOVER UN RECTÁNGULO CON LAS TECLAS DE FLECHA -----
rect_x = 50
rect_y = 50
speed = 1

'''while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar la pantalla con un color
    screen.fill((255, 255, 255))  # Blanco

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Dibujar el rectángulo en su nueva posición
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

    # Actualizar la pantalla
    pygame.display.flip()
'''
# ----- VERSIÓN 3: RECOLECTAR MONEDAS -----

x = 50
y = 50
speed = 1

coin = pygame.Rect(200,150,30,30)
player = pygame.Rect(x, y, 50,50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar la pantalla con un color
    screen.fill((255, 255, 255))  # Blanco

    # dibujar la moneda
    if coin:
        coin = pygame.draw.rect(screen, (255,255,0), (200,150,30,30))

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Dibujar el jugador en su nueva posición
    player = pygame.Rect(x,y,50,50)
    pygame.draw.rect(screen, (255,0,0), player)

    # si el rectángulo se mueve más allá del borde lo regresa
    if x < 0: x = 0
    if y < 0: y = 0
    if x > 700: x = 700
    if y > 500: y = 500

    if coin and player.colliderect(coin):
        print("Moneda recolectada")
        coin = None

    # Actualizar la pantalla
    pygame.display.flip()

'''# ----- VERSIÓN 4: LA MONEDA APARECE EN OTRO LUGAR -----

import pygame
import random

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Moneda")

# Player setup
x, y = 50, 50
speed = 1
player = pygame.Rect(x, y, 50, 50)

# Coin setup (random position)
coin = pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill((255, 255, 255))

    # Draw coin
    pygame.draw.rect(screen, (255, 255, 0), coin)

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Update player position
    player = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Boundaries
    if x < 0: x = 0
    if y < 0: y = 0
    if x > WIDTH-50: x = WIDTH-50
    if y > HEIGHT-50: y = HEIGHT-50

    # Collision check
    if player.colliderect(coin):
        print("Moneda recolectada")
        # Respawn coin at a new random location
        coin = pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30)

    # Update display
    pygame.display.flip()

pygame.quit()'''
