import sys
from pathlib import Path

import pygame

import settings

pygame.init()

CURRENT_DIR = Path(__file__).parent.resolve()

# Create the screen
screen = pygame.display.set_mode(size=(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
# Set the title
pygame.display.set_caption(settings.GAME_NAME)
# Init the clock
clock = pygame.time.Clock()

test_font = pygame.font.Font(CURRENT_DIR / "./assets/fonts/Pixeltype.ttf", 50)

# Create surfaces
sky_surf = pygame.image.load(CURRENT_DIR / "./assets/images/sky.png").convert()
ground_surf = pygame.image.load(CURRENT_DIR / "./assets/images/ground.png").convert()

score_surf = test_font.render("My Game", False, "black")
score_rect = score_surf.get_rect(center=(int(settings.WINDOW_WIDTH / 2), 50))

snail_surf = pygame.image.load(
    CURRENT_DIR / "./assets/images/snail/snail_1.png",
).convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load(
    CURRENT_DIR / "./assets/images/player/player_walk_1.png",
).convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION and player_rect.collidepoint(event.pos):
        #     print("Collision!")

    # Draw the screen
    screen.blit(sky_surf, dest=(0, 0))
    screen.blit(ground_surf, dest=(0, 300))
    screen.blit(score_surf, score_rect)

    # Move snail
    snail_rect.left -= 4
    if snail_rect.right <= 0:  # noqa: PLR2004
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    # Place player
    screen.blit(player_surf, player_rect)

    # Detect collision between player and snail
    # if player_rect.colliderect(snail_rect):
    #     print("Collision!")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("Collision!")

    # Update the screen
    pygame.display.update()
    clock.tick(settings.MAX_FPS)
