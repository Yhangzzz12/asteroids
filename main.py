# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from CircleShape import *

def main():
    pygame.get_init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # automatically put those objects in the group u set.
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH }')
    print(f'Screen height: {SCREEN_HEIGHT}')
    Ryan_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    aster_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for thing in drawable:
            thing.draw(screen)

        frame = clock.tick(60)
        dt = frame / 1000
        updatable.update(dt)


        for asteroid in asteroids:
            if  asteroid.check_for_collisions(Ryan_player):
                sys.exit('Game over!')
        
        for asteroid in asteroids:
            for each_bullet in shots:
                if asteroid.check_for_collisions(each_bullet):
                    asteroid.split()



            
        pygame.display.flip()


if __name__ == "__main__":
    main()
