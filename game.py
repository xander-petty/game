"""
A PyGame practice project
"""
__author__ = 'Xander Petty'

import pygame
import os
from mySprite import MySprite
from Bar import Bar
from Bar import generator as bar_generator
CLOCK = pygame.time.Clock()
TITLE = 'Practice Project'
RESOLUTION = (800, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('assets', 'Background_music.mp3'))
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(RESOLUTION)

def main():
    running = True
    pygame.mixer.music.play(loops=-1)
    player = MySprite((400, 300), screen)
    bar_group = pygame.sprite.Group()  
    projectiles = pygame.sprite.Group()
    while running:
        if len(bar_group) == 0:
            bar_group.add(bar_generator(7, 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    projectiles.add(player.fire())
                elif event.key == pygame.K_q:
                    running = False
        screen.fill(BLACK)
        player.update()
        bar_group.update() 
        projectiles.update()
        [projectile.check_collision(bar_group) for projectile in projectiles]
        player.draw(screen)
        bar_group.draw(screen) 
        projectiles.draw(screen)
        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()