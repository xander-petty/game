"""
A PyGame practice project
"""
__author__ = 'Xander Petty'

import pygame
from mySprite import MySprite
from Bar import Bar
from Bar import generator as bar_generator
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
    bars = bar_generator(7, 5)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        player.update()
        [bar.update() for bar in bars]
        [bar.draw(screen) for bar in bars]
        player.draw(screen)
        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()