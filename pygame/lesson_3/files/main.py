import sys
import pygame
import constants
from models import Player


def setup():
    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption(constants.WINDOW_TITLE)
    clock = pygame.time.Clock()
    return screen, clock


def main():
    screen, clock = setup()

    player = Player(
        p_initial_x=constants.WIDTH // 2,
        p_initial_y=constants.HEIGHT // 2,
        p_width=10,
        p_height=50,
        p_speed=1,
    )

    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input handling
        keys = pygame.key.get_pressed()
        vx = 0
        vy = 0

        if keys[pygame.K_LEFT]:
            vx = -player.get_speed()
        elif keys[pygame.K_RIGHT]:
            vx = player.get_speed()
        elif keys[pygame.K_UP]:
            vy = -player.get_speed()
        elif keys[pygame.K_DOWN]:
            vy = player.get_speed()

        player.set_velocity(vx, vy)

        # Drawing
        screen.fill(constants.BG_COLOR)
        player.update(screen)
        pygame.display.flip()

        clock.tick(constants.FPS)

    pygame.quit()
    sys.exit()


main()
