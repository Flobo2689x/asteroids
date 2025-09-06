import pygame
from constants import *
from player import *


def main():
    print("Starting Asteroids!\n")
    print(f"Screen width: {SCREEN_WIDTH}\n")
    print(f"Screen height: {SCREEN_HEIGHT}\n")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        #GO
        player.update(dt)
        player.draw(screen)


        #REFRESH
        pygame.display.flip()
        #WAIT
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
