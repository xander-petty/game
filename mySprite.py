"""A simple sprite to move around.
"""
__author__ = 'Xander Petty'

import pygame
import os
from Projectile import Projectile

class MySprite(pygame.sprite.Sprite):
    def __init__(self, position, surface):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'smile.png'))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = pygame.math.Vector2(0, 0)
        self.surface_rect = surface.get_rect()

    def fire(self):
        return Projectile(self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.rect.y > 0:
                self.rect.y -= 5
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.rect.y < self.surface_rect.height - self.rect.height:
                self.rect.y += 5
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x > 0:
                self.rect.x -= 5
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x < self.surface_rect.width - self.rect.width:
                self.rect.x += 5
        self.rect.move_ip(self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)