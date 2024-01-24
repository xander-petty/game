import unittest
import pygame
import os
import sys
os.chdir(os.path.abspath(os.pardir))
sys.path.append(os.getcwd())
from mySprite import MySprite

class TestMySprite(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.position = (100, 100)
        self.sprite = MySprite(self.position)

    def test_initial_position(self):
        self.assertEqual(self.sprite.rect.center, self.position)

    def test_move_up(self):
        self.sprite.speed = pygame.math.Vector2(0, -5)
        self.sprite.update()
        self.assertEqual(self.sprite.rect.center, (100, 95))

    def test_move_down(self):
        self.sprite.speed = pygame.math.Vector2(0, 5)
        self.sprite.update()
        self.assertEqual(self.sprite.rect.center, (100, 105))

    def test_move_left(self):
        self.sprite.speed = pygame.math.Vector2(-5, 0)
        self.sprite.update()
        self.assertEqual(self.sprite.rect.center, (95, 100))

    def test_move_right(self):
        self.sprite.speed = pygame.math.Vector2(5, 0)
        self.sprite.update()
        self.assertEqual(self.sprite.rect.center, (105, 100))

    def test_shoot(self):
        projectile = self.sprite.fire()
        self.assertEqual(projectile.rect.center, self.sprite.rect.center)

    def test_update(self):
        self.sprite.speed = pygame.math.Vector2(5, 0)
        self.sprite.update()
        self.assertEqual(self.sprite.rect.center, (105, 100))

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()