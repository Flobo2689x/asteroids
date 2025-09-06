from hmac import new
import pygame
from constants import *
from circleshape import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, (155,155,155), self.position, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randAngle1 = self.velocity.rotate(random.uniform(20,50))
            randAngle2 = self.velocity.rotate(random.uniform(20,50))
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, newRadius)
            split2 = Asteroid(self.position.x, self.position.y, newRadius)
            split1.velocity = randAngle1*1.2
            split2.velocity = randAngle2*1.6