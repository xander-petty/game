"""A simple sprite to move around.
"""
__author__ = 'Xander Petty'

import pygame
import os
from Projectile import Projectile

class MySprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'smile.png'))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = pygame.math.Vector2(0, 0)

    def fire(self):
        return Projectile(self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 5
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 5
        self.rect.move_ip(self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)