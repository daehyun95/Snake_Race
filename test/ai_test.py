import sys
sys.path.append("..")  # Lets us import from the parent directory
from ai import AI  # nopep8
from game_controller import GameController  # nopep8
from gui_controls import GUI_Controls  # nopep8
from apple import Apple  # nopep8
from snake import Snake  # nopep8


shared_ui_control = GUI_Controls()
UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


def test_constructor():
    # Field coords are arbitrary
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_ai = AI(test_gc)
    assert test_ai._gc == test_gc


def test_update():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_ai = AI(test_gc)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    test_ai.set_snake(test_snake)
    pos = (test_snake.body[0].x, test_snake.body[0].y)
    test_gc._apple = Apple(test_snake.body[0].x, test_snake.body[0].y - 2)
    test_ai.update()
    assert test_snake._dir == 'UP'


def test_choose_dir():
    """
    Test the direction choosing functionality
    Human snake is keep moving left
    Ai snake needs to avoid getting hit by human snake and
    needs to move in the direction to the apple
    """
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_ai = AI(test_gc)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    test_ai.set_snake(test_snake)
    # Apple is at the higher position
    # Ai snake should choose UP direction
    test_gc._apple = Apple(test_snake.body[0].x, test_snake.body[0].y - 2)
    assert test_ai._choose_dir() == UP
    test_gc._apple = Apple(test_snake.body[0].x - 3, test_snake.body[0].y - 3)
    assert test_ai._choose_dir() == UP
    # Apple is at the lower position
    # Ai snake should choose DOWN direction
    test_gc._apple = Apple(test_snake.body[0].x, test_snake.body[0].y + 2)
    assert test_ai._choose_dir() == DOWN
    test_gc._apple = Apple(test_snake.body[0].x + 3, test_snake.body[0].y + 3)
    assert test_ai._choose_dir() == DOWN


def test_get_neighbor_coord():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_ai = AI(test_gc)
    test_snake = Snake(test_gc, 'Human', shared_ui_control)
    test_ai.set_snake(test_snake)
    up_dir = (test_ai._snake.body[0].x, test_ai._snake.body[0].y-1)
    UP = 38
    assert test_ai._get_neighbor_coord(UP) == up_dir


def test_min_dist():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_ai = AI(test_gc)
    p1 = (0, 5)
    p2 = (0, 10)
    assert test_ai._min_dist(p1, p2) == 5
    print(test_gc.h)
    p1 = (0, 10)
    p2 = (0, 1)
    assert test_ai._min_dist(p1, p2) == 1


def test_clear_score():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_ai = AI(test_gc)
    arbitrary_coord = (10, 10)
    assert test_ai._clear_score(arbitrary_coord) == 1
    test_gc.set_deadly_points([arbitrary_coord])
    print(test_gc._deadly_points)
    assert test_ai._clear_score(arbitrary_coord) == -1


def test_apple_distance():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    apple_coords = (0, 60)
    test_gc._apple = Apple(*apple_coords)
    dist_coords = (0, 55)
    test_ai = AI(test_gc)
    # min dist is 5, converted to score 145
    assert test_ai._apple_distance(dist_coords) == 145


def test_convert_min_to_score():
    arg = 5
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    # gc.square_size == 20
    test_ai = AI(test_gc)
    score = test_ai._convert_min_to_score(arg)
    # (test_gc._w * test_gc._h) - arg
    assert score == 145
