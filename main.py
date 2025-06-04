# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    dt = 0
    gameplay = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player object at the center of the screen

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable_group = pygame.sprite.Group(player)
    drawable_group = pygame.sprite.Group(player)
    Player.containers = (updatable_group, drawable_group)

    while gameplay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")  # Fill the screen with black color
        updatable_group.update(dt)
        for drawable in drawable_group:
            drawable.draw(screen)  # Draw the drawable objects
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()