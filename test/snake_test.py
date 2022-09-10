import sys
sys.path.append("..")  # Lets us import from the parent directory
from snake import Snake  # nopep8
from gui_controls import GUI_Controls  # nopep8
from game_controller import GameController  # nopep8
from apple import Apple  # nopep8

shared_ui_control = GUI_Controls()
UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


def test_constructor():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    assert len(test_snake._body) == test_snake._len


def test_control():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    test_snake.control(UP)
    assert test_snake._dir == 'UP'
    test_snake.control(RIGHT)
    assert test_snake._dir == 'RIGHT'
    test_snake.control(LEFT)
    assert test_snake._dir == 'RIGHT'


def test_shrink():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    before_length = len(test_snake.body)
    test_snake.shrink()
    assert len(test_snake.body) == before_length - 1


def test_update_move():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    snake_head_pos = (test_snake.body[0].x, test_snake.body[0].y)
    do_move = False
    test_snake._update_move(False)
    assert (test_snake.body[0].x, test_snake.body[0].y) == snake_head_pos
    test_snake._update_move(True)
    new_snake_head_pos = (snake_head_pos[0] - 1, snake_head_pos[1])
    assert (test_snake.body[0].x, test_snake.body[0].y) == new_snake_head_pos


def test_move_head():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    snake_head_pos = (test_snake.body[0].x, test_snake.body[0].y)
    test_snake._move_head()
    new_snake_head_pos = (snake_head_pos[0] - 1, snake_head_pos[1])
    assert (test_snake.body[0].x, test_snake.body[0].y) == new_snake_head_pos


def test_evaluate_head_placement():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    test_gc._human_snake = test_snake
    assert not hasattr(test_gc, '_winner')
    test_snake._evaluate_head_placement()
    assert test_gc._winner._player == 'AI'


def test_set_dir():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    test_snake._set_dir('UP')
    assert test_snake._dir == 'UP'
    assert test_snake._x_dir == 0
    assert test_snake._y_dir == -1
    test_snake._set_dir('RIGHT')
    assert test_snake._dir == 'RIGHT'
    assert test_snake._x_dir == 1
    assert test_snake._y_dir == 0
    test_snake._set_dir('DOWN')
    assert test_snake._dir == 'DOWN'
    assert test_snake._x_dir == 0
    assert test_snake._y_dir == 1
    test_snake._set_dir('LEFT')
    assert test_snake._dir == 'LEFT'
    assert test_snake._x_dir == -1
    assert test_snake._y_dir == 0


def test_body():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    expected_length = test_snake._len
    assert len(test_snake.body) == expected_length
    assert test_snake.body[0].__class__.__name__ == 'SnakeSquare'


def test_player():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    assert test_snake.player == 'Human'
