class SnakeController:
    """
    Abstract class for controlling snake
    """

    # This class will not be instantiated,
    # but will be extended by fully implemented
    # snake controllers for AI and humman control,
    # which will inherit this class's methods.

    # Public methods
    def set_snake(self, snake):
        """
        Set the snake that will be controlled
        by this controller
        Snake --> None
        """
        self._snake = snake

    def control_snake(self, direction):
        """
        Give the snake a direction to go
        Direction --> None
        """
        self._snake.control(direction)
