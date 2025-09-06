import pygame
from constants import *
from circleshape import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 5

    def draw(self, screen):
        return pygame.draw.circle(screen, (255,155,155), self.position, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)