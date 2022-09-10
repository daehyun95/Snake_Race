from snake_controller import SnakeController


class GUI_Controls(SnakeController):
    """
    Snake controller for human player using
    GUI input
    """

    # Public methods
    def key_pressed(self, key_code):
        """
        Control snake with keyboard input
        KeyCode --> None
        """
        self.control_snake(key_code)
