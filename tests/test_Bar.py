import unittest
import pygame
import os
import sys
os.chdir(os.path.abspath(os.pardir))
sys.path.append(os.getcwd())
from Bar import Bar

class TestBar(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.position = (100, 100)
        self.bar = Bar(self.position)

    def test_initial_position(self):
        self.assertEqual(self.bar.rect.center, self.position)

    def test_update(self):
        self.bar.speed = pygame.math.Vector2(5, 0)
        self.bar.update()
        self.assertEqual(self.bar.rect.center, (105, 100))

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()