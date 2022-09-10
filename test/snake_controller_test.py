import sys
sys.path.append("..")  # Lets us import from the parent directory
from snake import Snake  # nopep8
from gui_controls import GUI_Controls  # nopep8
from game_controller import GameController  # nopep8


UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


def test_set_snake():
    test_coords = (300, 200)
    # GUI_Controls extends SnakeController
    test_ui_control = GUI_Controls()
    test_gc = GameController(test_coords, test_ui_control)
    # set_snake() is called in the Snake constructor
    test_snake = Snake(test_gc, 'Human', test_ui_control)
    assert test_ui_control._snake.__class__.__name__ == 'Snake'
    assert test_ui_control._snake._player == 'Human'


def test_control_snake():
    test_coords = (300, 200)
    test_ui_control = GUI_Controls()
    test_gc = GameController(test_coords, test_ui_control)
    test_snake = Snake(test_gc, 'Human', test_ui_control)
    test_ui_control.control_snake(DOWN)
    assert test_snake._dir == 'DOWN'
    test_ui_control.control_snake(RIGHT)
    assert test_snake._dir == 'RIGHT'
