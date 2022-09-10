import sys
sys.path.append("..")  # Lets us import from the parent directory
from crash import Crash  # nopep8


def test_constructor():
    crash_coords = (5, 10)
    test_crash = Crash(*crash_coords)
    assert test_crash._x == 5
    assert test_crash._y == 10
