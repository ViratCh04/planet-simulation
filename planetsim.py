import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1350, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_GREY = (80, 78, 81)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU    # 1 AU = 100 pixels
    TIMESTEP = (60*60) * 24 # 1 day in seconds

def main():
    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(60)
        WINDOW.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


main()