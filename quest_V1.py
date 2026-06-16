import pygame

pygame.init()

scr_ancho = 600
scr_alto = 400
screen = pygame.display.set_mode((scr_ancho,scr_alto))
pygame.display.set_caption("Mi juego de misiones")

# Diseño
col_azul_os = "#0E4378"
col_azul_claro = "#4D93DA"
col_verde = "#0E7820"
col_cafe = "#5E3920"
col_vino = "#490D0D"
col_morado = "#760C80"

font = pygame.font.SysFont("Arial", 24)

# Cambiar el ícono de la ventana
icono = pygame.image.load("IMAGENES/icon.png")
pygame.display.set_icon(icono)

# Fondo de la pantalla
# transformar a archivo de pixeles
fondo_original = pygame.image.load("IMAGENES/fondo1.jpg").convert()
# escalar a la pantalla
fondo = pygame.transform.scale(fondo_original, (scr_ancho, scr_alto))

# Frame rate
clock = pygame.time.Clock()

# Movimiento de los objetos
x, y = 100, 100 # coordenadas iniciales
speed = 10 # velocidad de mov.

# ----- FUNCIONES -----

# Ventana emergente (popup)
show_popup = False
popup_rect = pygame.Rect(300,100,100,40)
close_button_rect = pygame.Rect(300,100,100,40)

# diferencia entre rect y Rect: el rect es un objeto que tiene atributos como x, y, width, height, etc.
# El Rect es una clase que se utiliza para crear objetos rectangulares con argumentos como posicion (tuplas: topleft, midtop, etc.) y tamaño (width, height).
# El Rect también tiene métodos para detectar colisiones, mover el rectángulo, etc.

def draw_popup():
    pygame.draw.rect(screen, col_azul_claro, popup_rect)
    pygame.draw.rect(screen, col_cafe, popup_rect, 4) # borde

    # texto de la ventana
    text_sup = font.render("Ventana emergente", True, col_azul_os)
    text_rect = text_sup.get_rect(center=(popup_rect.centerx, popup_rect.centery -30))

    # cerrar ventana
    pygame.draw.rect(screen, col_vino, close_button_rect)
    btn_texto = font.render("Cerrar", True, "white")
    btn_texto_rect = btn_texto.get_rect(center=close_button_rect.center)

    screen.blit(btn_texto, btn_texto_rect)

# ------------------------------ CICLO DE JUEGO ------------------------------
running = True
while running:

    #screen.fill("#7A9BBF") # solo llenar con color
    screen.blit(fondo, (0,0)) # llenar pantalla con la imagen
    pygame.draw.circle(screen, "#125612", [200, 60], 16, 0)

    mouse_pos = pygame.mouse.get_pos()
    
    if not show_popup:
        prompt_text = font.render("Presiona la tecla de ESPACIO para abrir ventana", True, col_cafe)
        screen.blit(prompt_text, (150, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < scr_ancho:
                x += speed
            elif event.key == pygame.K_LEFT and x > 0:
                x -= speed
            elif event.key == pygame.K_DOWN and y < scr_alto:
                y += speed
            elif event.key == pygame.K_UP and y > 0:
                y -= speed
            
            elif event.key == pygame.K_SPACE:
                show_popup = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # click izquierdo
                if show_popup and close_button_rect.collidepoint(mouse_pos):
                    show_popup = False
                
    if show_popup:
        draw_popup()
         
    pygame.draw.rect(screen, "#401D04", [x, y, 55,55], 0)
    
    pygame.display.update()
    clock.tick(60) # frame rate 60 segundos

pygame.quit()