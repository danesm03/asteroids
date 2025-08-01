import pygame
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)


        screen.fill((0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)

        for ast in asteroids:
            #print(f"ast position:{ast.position} player position:{player.position}")
            if ast.collision_check(player) == True:
                print("Game Over!")
                sys.exit()

            for bullet in shots:
                if bullet.collision_check(ast) == True:
                    bullet.kill()
                    ast.split()

        
        

        pygame.display.flip()
    
        #limit framerate to 60fps
        dt = clock.tick(60) / 1000
       #print(f"dt:{dt}")

if __name__ == "__main__":
    main()
