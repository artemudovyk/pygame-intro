import sys

import pygame

import settings

pygame.init()

# Create the screen
screen = pygame.display.set_mode(size=(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
# Set the title
pygame.display.set_caption(settings.GAME_NAME)
# Init the clock
clock = pygame.time.Clock()

test_font = pygame.font.Font("./assets/fonts/Pixeltype.ttf", 50)

# Create surfaces
sky_surface = pygame.image.load("./assets/images/sky.png")
ground_surface = pygame.image.load("./assets/images/ground.png")
score_surface = test_font.render("My Game", False, "black")

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, dest=(0, 0))
    screen.blit(ground_surface, dest=(0, 300))
    screen.blit(score_surface, dest=(350, 50))

    # Update the screen
    pygame.display.update()
    clock.tick(settings.MAX_FPS)
