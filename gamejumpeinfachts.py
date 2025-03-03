import pygame

# Initialisierung
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump 'n' Run")

# Farben
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Spielfigur
player = pygame.Rect(100, 500, 40, 40)
velocity_x = 0
velocity_y = 0
gravity = 0.5
jump_power = -10
on_ground = False

# Plattform
ground = pygame.Rect(0, 550, WIDTH, 50)

# Spiel-Loop
running = True
while running:
    pygame.time.delay(30)  # FPS-Begrenzung
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Steuerung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        velocity_x = 5
    else:
        velocity_x = 0

    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power
        on_ground = False

    # Physik
    velocity_y += gravity
    player.x += velocity_x
    player.y += velocity_y

    # Kollision mit Boden
    if player.colliderect(ground):
        player.y = ground.y - player.height
        velocity_y = 0
        on_ground = True

    # Bildschirm aktualisieren
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, (0, 255, 0), ground)
    pygame.display.update()

pygame.quit()