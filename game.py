"""
A PyGame practice project
"""
__author__ = 'Xander Petty'

import pygame
from mySprite import MySprite
CLOCK = pygame.time.Clock()
TITLE = 'Practice Project'
RESOLUTION = (800, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(RESOLUTION)

def main():
    running = True
    player = MySprite((400, 300))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        player.update()
        player.draw(screen)
        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()