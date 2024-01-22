"""
The projectile object that will be fired by the player
"""
__author__ = 'Xander Petty'

import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('shoot.png')
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)

    def move_up(self):
        self.rect.y -= 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)