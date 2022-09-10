from game_controller import GameController
from gui_controls import GUI_Controls

PIXEL_WIDTH = 600
PIXEL_HEIGHT = 600
BG_COLOR = (0.0, 0.6, 0.4)

field = (PIXEL_WIDTH, PIXEL_HEIGHT)
gui_control = GUI_Controls()
gc = GameController(field, gui_control)


def setup():
    """
    Set up the environment
    """
    size(*field)
    colorMode(RGB, 1)


def draw():
    """
    Update the environment
    """
    if gc.playing:
        background(*BG_COLOR)
        gc.update()
    else:
        gc.end_text()
    gc.allowKeyPress = True


def keyPressed():
    if key == CODED and gc.allowKeyPress:
        # Ensure that only one key press
        # event can happen during a single
        # draw cycle
        gc.allowKeyPress = False
        gui_control.key_pressed(keyCode)
