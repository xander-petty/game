# Practice Project

This is a simple game project using Pygame. The game displays a sprite on the screen.

## Getting Started

Create a Python virtual environment
```bash
python3 -m venv .
source ./bin/activate
```

Update pip
```bash
pip install --upgrade pip setuptools
```

### Prerequisites

Ensure requirements are met by installing packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### Running the Game

To run the game, navigate to the directory containing the game.py file and run:

```bash
python game.py
```

## Game Details

The game initializes a Pygame screen with a resolution of 800x600. A sprite is loaded from a file named 'smile.png' and is drawn on the screen at the coordinates (400, 300). The game runs in a loop until the Pygame QUIT event is triggered, such as when the game window is closed.

## Code Structure

- `game.py`: This is the main file that runs the game.
- `mySprite.py`: This file contains the MySprite class used to create and manage the sprite in the game.
- `Bar.py`: This is the bar object that will be shot at.
- `Projectile.py`: This is the object that will be fired from the player.

## Test Units
- `test_game.py`: Unit test for the game loop.
- `test_mySprite.py`: Unit test for the mySprite object.
- `test_Bar.py`: Unit test for the Bar object.
- `test_Projectile.py`: Unit test for the projectile object.

## Built With

- [Pygame](https://www.pygame.org/news) - The game engine used

## Authors

- Xander Petty

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.