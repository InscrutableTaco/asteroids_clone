# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    clock = pygame.time.Clock()
    dt = 0



    print_debug = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #print(player)  # This should print something like <Player object at 0x...>
        print(isinstance(player, CircleShape))

        print(player.__class__)
        print(player.__class__.__bases__)

        player.test_method()
        screen.fill(000000, rect=None, special_flags=0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            shots.add(shot)

        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()

        if print_debug == True:
            print(f"player position = {player.position}")
            print_debug = False

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
