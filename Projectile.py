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
        self.fired = True

    def _return_coverage(self):
        x_range = range(self.rect.x, self.rect.x + self.rect.width)
        y_range = range(self.rect.y, self.rect.y + self.rect.height)
        return (x_range, y_range)
    
    def check_collision(self, sprite_group):
        for sprite in sprite_group:
            if sprite.rect.colliderect(self.rect):
                return True

    def update(self):
        self.rect.move_ip(self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)