import sys
sys.path.append("..")  # Lets us import from the parent directory
from game_controller import GameController  # nopep8
from gui_controls import GUI_Controls  # nopep8
from snake_square import SnakeSquare  # nopep8


shared_ui_control = GUI_Controls()


def test_constructor():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    assert test_gc._pix_w == test_coords[0]
    assert test_gc._pix_h == test_coords[1]
    assert test_gc._w == test_gc._pix_w//test_gc.SQUARE_SIZE
    assert test_gc._h == test_gc._pix_h//test_gc.SQUARE_SIZE
    assert test_gc._ai_control.__class__.__name__ == 'AI'
    assert test_gc._ai_snake.__class__.__name__ == 'Snake'
    assert test_gc._human_snake.__class__.__name__ == 'Snake'
    assert not test_gc._counter % test_gc._speed_control


def test_set_apple():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_gc.set_apple()
    assert test_gc._apple.__class__.__name__ == 'Apple'
    assert test_gc._apple._x <= test_gc._w
    assert test_gc._apple._y <= test_gc._h


def test_end_game():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    assert not hasattr(test_gc, '_winner')
    assert not hasattr(test_gc, '_loser')
    test_locatition = (1, 2)
    test_gc.end_game(event='Collision', location=test_locatition)
    assert test_gc._winner.__class__.__name__ == 'Snake'
    assert test_gc._loser.__class__.__name__ == 'Snake'
    assert test_gc._winner is not test_gc._loser
    assert test_gc._end_event == 'Collision'
    assert test_gc._end_location == test_locatition
    assert not test_gc._playing


def test_set_deadly_points():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    snakes_only = len(test_gc._deadly_points)
    new_deadly_points = [(0, 0), (300, 200)]
    test_gc.set_deadly_points(new_deadly_points)
    assert len(test_gc._deadly_points) == snakes_only + 2
    assert new_deadly_points[0] in test_gc._deadly_points
    assert new_deadly_points[1] in test_gc._deadly_points


def test_add_deadly_point():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    snakes_only = len(test_gc._deadly_points)
    new_deadly_point = (0, 0)
    test_gc.add_deadly_point(new_deadly_point)
    assert len(test_gc._deadly_points) == snakes_only + 1
    assert new_deadly_point in test_gc._deadly_points


def test_remove_deadly_point():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    snakes_only = len(test_gc._deadly_points)
    new_deadly_point = (0, 0)
    test_gc.add_deadly_point(new_deadly_point)
    assert len(test_gc._deadly_points) == snakes_only + 1
    assert new_deadly_point in test_gc._deadly_points
    test_gc.remove_deadly_point(new_deadly_point)
    assert len(test_gc._deadly_points) == snakes_only
    assert new_deadly_point not in test_gc._deadly_points


def test_apple_eat():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    other_length = len(test_gc._ai_snake._body)
    test_gc.apple_eat(test_gc._human_snake)
    new_other_length = len(test_gc._ai_snake._body)
    assert new_other_length == other_length - 1


def test_random_coords():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    coords = test_gc._random_coords()
    assert len(coords) == 2
    assert coords[0] <= test_coords[0] and coords[0] >= 0
    assert coords[1] <= test_coords[1] and coords[0] >= 0
    assert type(coords[0]) is int
    assert type(coords[1]) is int


def test_same_loc():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    s1_args = (100, 200, 1)
    s2_args = (200, 200, 0)
    s3_args = (100, 200, 0)
    ss1 = SnakeSquare(*s1_args)
    ss2 = SnakeSquare(*s2_args)
    ss3 = SnakeSquare(*s3_args)
    assert test_gc._same_loc(ss1, ss3)
    assert not test_gc._same_loc(ss1, ss2)


def test_h_getter():
    pwidth = 300
    pheight = 200
    test_gc = GameController((pwidth, pheight), shared_ui_control)
    h = pheight/test_gc.SQUARE_SIZE
    assert test_gc.h == h


def test_w_getter():
    pwidth = 300
    pheight = 200
    test_gc = GameController((pwidth, pheight), shared_ui_control)
    w = pwidth/test_gc.SQUARE_SIZE
    assert test_gc.w == w


def test_playing_getter():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    assert test_gc.playing


def test_deadly_points_getter():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    expected_points = {
        (10, 5), (5, 5), (1, 5), (4, 5),
        (11, 5), (12, 5), (2, 5), (13, 5),
        (3, 5), (14, 5)
        }
    assert test_gc.deadly_points == expected_points


def test_playing_getter():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_gc.set_apple()
    assert test_gc.apple.__class__.__name__ == 'Apple'
    assert test_gc.apple._x <= test_gc._w
    assert test_gc.apple._y <= test_gc._h


def test_playing_getter():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_gc.set_apple()
    assert len(test_gc.apple_location) == 2
    assert test_gc.apple_location[0] <= test_gc._w
    assert test_gc.apple_location[1] <= test_gc._h


def test_playing_getter():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    assert test_gc.allowKeyPress.__class__.__name__ == 'bool'


def test_playing_getter():
    test_coords = (300, 200)
    test_gc = GameController(test_coords, shared_ui_control)
    test_gc.allowKeyPress = True
    assert test_gc.allowKeyPress
    test_gc.allowKeyPress = False
    assert not test_gc.allowKeyPress
