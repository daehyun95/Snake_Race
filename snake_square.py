class SnakeSquare(object):
    """
    A single square part of the snake's body
    """
    def __init__(self, x, y, dot_color):
        """
        Initialize square
        Number Number Color --> SnakeSquare
        """
        self._x = x
        self._y = y
        self._dot_color = dot_color
        self._WHITE = 1.0
        self._BLACK = 0.0
        self._YELLOW = (1, 1, 0)
        self._SQUARE_SIZE = 20
        self._OFFSET = 10
        self._ELLIPSE_SIZE = 8

    def display(self):
        strokeWeight(1)
        fill(self._BLACK)
        stroke(self._WHITE)
        square(self._x*self._SQUARE_SIZE,
               self.y*self._SQUARE_SIZE,
               self._SQUARE_SIZE)
        stroke(*self._YELLOW)
        fill(*self._dot_color)
        ellipse(self._x*self._SQUARE_SIZE+self._OFFSET,
                self.y*self._SQUARE_SIZE+self._OFFSET,
                self._ELLIPSE_SIZE,
                self._ELLIPSE_SIZE)

    # Getters and setters
    @property
    def x(self):
        """
        Getter for x value
        None --> Number
        """
        return self._x

    @x.setter
    def x(self, val):
        """
        Setter for x value
        Number --> None
        """
        self._x = val

    @property
    def y(self):
        """
        Getter for y value
        None --> Number
        """
        return self._y

    @y.setter
    def y(self, val):
        """
        Setter for y value
        Number --> None
        """
        self._y = val
