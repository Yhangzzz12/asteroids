from CircleShape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20,50)
            velocity_1 = self.velocity.rotate(random_angle)
            velocity_2 = self.velocity.rotate(-random_angle)
            self_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid_1 = Asteroid(self.position.x, self.position.y, self_radius)
            Asteroid_2 = Asteroid(self.position.x, self.position.y, self_radius)
            Asteroid_1.velocity = velocity_1 * 1.2
            Asteroid_2.velocity = velocity_2 * 1.2






