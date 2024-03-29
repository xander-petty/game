"""
The projectile object that will be fired by the player
"""
__author__ = 'Xander Petty'

import pygame
import os

class Projectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'projectile.png'))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = pygame.math.Vector2(0, 0)
        self.fired = True
        pygame.mixer.Sound(os.path.join('assets', 'weapon_fire.mp3')).play()
    
    def check_collision(self, sprite_group):
        for sprite in sprite_group:
            if sprite.rect.colliderect(self.rect):
                pygame.mixer.Sound(os.path.join('assets', 'crash.mp3')).play()
                sprite.kill()
                self.kill()

    def update(self):
        self.rect.move_ip(self.speed)
        if self.fired and self.rect.y > 0:
            self.rect.y -= 5
        else:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)