import pygame
from random import randint
# versión más actualizada: pip install pygame-ce para usar FRect

# Ejercicio 1: Importar meteoro y centrarlo en pantalla
# Ejercicio 2: Importar láser y ponerlo en la esquina inferior izquierda con padding 20px
# Ejercicio 3: Que el jugador rebote de derecha a izquierda

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tutorial 1: Space Shooter")
running = True

# crear surface para mostrar gráficos
surface = pygame.Surface((100,200))
surface.fill("green")

# crear una animación simple
x = 100 # variables para la posición del rectángulo
y = 100

# importar una imagen
player_surf = pygame.image.load("IMAGENES/dino2.png").convert_alpha() # convert_alpha para conservar transparencia
player_surf = pygame.transform.scale(player_surf, (50,50)) # escalar la imagen

# crear un rectángulo a partir de la imagen para detectar colisiones
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)) # rectángulo que contiene la figura y está centrado en (x,y)

# importar estrella y poner 20 sobre la pantalla de forma aleatoria
star_surf = pygame.image.load("IMAGENES/star_icon.png").convert_alpha()
star_surf = pygame.transform.scale(star_surf, (40,40))

# crear una tupla con las posiciones de las estrellas
star_positions = [(randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

# ----- JUEGO -----
meteor_surf = pygame.image.load("IMAGENES/asteroidicon.png").convert_alpha()
meteor_surf = pygame.transform.scale(meteor_surf, (50,50))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) # centrado en pantalla

laser_surf = pygame.image.load("IMAGENES/lightsaber1.png").convert_alpha()
laser_surf = pygame.transform.scale(laser_surf, (50,50))
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT-20))

player_direction = -1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("darkgray")

    # poner estrellas aleatoriamente sobre la pantalla
    
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # mostrar la nave sobre las estrellas
    #x += 0.05 # variar la coordenada de la nave en cada ciclo de juego
    #display_surface.blit(player_surf, (x, y)) 
    #player_rect.left += 0.1 # mover el rectángulo de la nave a la derecha
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    #display_surface.blit(player_surf, player_rect) # el jugador siempre queda encima

    # Añadir movimiento (rebote) al jugador

    player_rect.x += player_direction*0.4
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1

    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()