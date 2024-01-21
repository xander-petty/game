import unittest
import pygame
from mySprite import MySprite

class TestMySprite(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.image = pygame.Surface([50, 50])
        self.position = (100, 100)
        self.sprite = MySprite(self.image, self.position)

    def test_initial_position(self):
        self.assertEqual(self.sprite.rect.center, self.position)

    def test_update(self):
        self.sprite.speed = pygame.math.Vector2(5, 0)
        self.sprite.update()
        self.assertEqual(self.sprite.rect.center, (105, 100))

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()