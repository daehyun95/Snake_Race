import sys
sys.path.append("..")  # Lets us import from the parent directory
from apple import Apple  # nopep8


def test_constructor():
    apple_coords = (5, 10)
    test_apple = Apple(*apple_coords)
    assert test_apple.x == 5
    assert test_apple.y == 10
