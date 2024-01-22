"""A bar object to be shot
"""
__author__ = 'Xander Petty'

import pygame

def generator(count, rows):
    multiplier = 100
    bars = []
    for row in range(rows):
        y_pos = row * (multiplier / 4) + multiplier
        for bar in range(count):
            x_pos = (bar * multiplier) + multiplier
            bars.append(Bar((x_pos, y_pos)))
    return bars

class Bar(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('bar.png')
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)