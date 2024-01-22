import unittest
import pygame
from Projectile import Projectile

class TestProjectile(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.position = (100, 100)
        self.missle = Projectile(self.position)

    def test_initial_position(self):
        self.assertEqual(self.missle.rect.center, self.position)

    def test_update(self):
        self.missle.speed = pygame.math.Vector2(5, 0)
        self.missle.update()
        self.assertEqual(self.missle.rect.center, (105, 100))

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()