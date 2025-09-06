import pygame
from constants import *


def main():
    print("Starting Asteroids!\n")
    print(f"Screen width: {SCREEN_WIDTH}\n")
    print(f"Screen height: {SCREEN_HEIGHT}\n")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #REFRESH
        pygame.display.flip()


if __name__ == "__main__":
    main()
