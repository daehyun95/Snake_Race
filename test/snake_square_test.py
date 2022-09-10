import sys
sys.path.append("..")  # Lets us import from the parent directory
from snake_square import SnakeSquare  # nopep8


def test_constructor():
    dot_color = (1.0, 0.0, 0.0)
    x = 5
    y = 10
    test_snakes_square = SnakeSquare(x, y, dot_color)
    assert test_snakes_square._x == 5
    assert test_snakes_square._y == 10


def test_setters_and_getters():
    dot_color = (1.0, 0.0, 0.0)
    x = 5
    y = 10
    test_snakes_square = SnakeSquare(x, y, dot_color)
    new_x = 20
    test_snakes_square.x = new_x
    assert test_snakes_square.x == new_x
    new_y = 15
    test_snakes_square.y = new_y
    assert test_snakes_square.y == new_y