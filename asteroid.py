import pygame
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, (155,155,155), self.position, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)