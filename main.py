import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting Asteroids!\n")
    print(f"Screen width: {SCREEN_WIDTH}\n")
    print(f"Screen height: {SCREEN_HEIGHT}\n")
    pygame.init()


    #GROUPS
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updateable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (drawable, updateable, shots)

    #CREATE GAME OBJECTS
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        #GO
        updateable.update(dt)
        
        for drawables in drawable:
            drawables.draw(screen)

        #COLLISION CHECK
        for asteroid in asteroids:
            if player.collisonCheck(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.collisonCheck(asteroid):
                    asteroid.split()
                    shot.kill()
                

        #REFRESH
        pygame.display.flip()
        #WAIT
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
