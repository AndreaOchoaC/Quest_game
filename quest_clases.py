import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Mi juego de misiones")

# Cambiar el ícono de la ventana
icono = pygame.image.load("IMAGENES/icon.png")
pygame.display.set_icon(icono)

# Ciclo de juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("#7A9BBF")
    pygame.draw.rect(screen, "#111111", [50, 50,150,100], 0)
    pygame.draw.circle(screen, "#125612", [300, 200], 50, 0)
    pygame.draw.polygon(screen, "#D89932", [[200,200], [200,300], [100,300]], 5)
    pygame.draw.line(screen, "red", [200,350], [500,350], 4)

    pygame.display.update()

pygame.quit()