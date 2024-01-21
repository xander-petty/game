import unittest
import pygame
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = game

    def test_initialization(self):
        self.assertEqual(self.game.TITLE, 'Practice Project')
        self.assertEqual(self.game.RESOLUTION, (800, 600))
        self.assertEqual(self.game.BLACK, (0, 0, 0))
        self.assertEqual(self.game.WHITE, (255, 255, 255))

    def test_game_loop(self):
        self.game.running = True
        self.game.pygame.event.post(pygame.event.Event(pygame.K_UP))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_w))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_DOWN))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_s))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_LEFT))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_a))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_RIGHT))
        self.game.pygame.event.post(pygame.event.Event(pygame.K_d))
        self.game.pygame.event.post(pygame.event.Event(pygame.QUIT))
        self.game.main()  # This should run the game loop until pygame.QUIT is posted

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()