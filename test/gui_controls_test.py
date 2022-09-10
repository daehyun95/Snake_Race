import sys
sys.path.append("..")  # Lets us import from the parent directory
from snake import Snake  # nopep8
from gui_controls import GUI_Controls  # nopep8
from game_controller import GameController  # nopep8


UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


def test_key_pressed():
    test_coords = (300, 200)
    test_ui_control = GUI_Controls()
    test_gc = GameController(test_coords, test_ui_control)
    test_snake = Snake(test_gc, 'Human', test_ui_control)
    test_ui_control.key_pressed(UP)
    assert test_snake._dir == 'UP'
    test_ui_control.key_pressed(RIGHT)
    assert test_snake._dir == 'RIGHT'
