class Crash:
    """
    The crash bang visual element
    """
    def __init__(self, x, y):
        """
        Initialize a crash bang at coordinates
        Number, Number --> None
        """
        self._x = x
        self._y = y
        self._SQUARE_SIZE = 20
        self._OFFSET = 10
        self._YELLOW = (1, 1, 0)

    # Public methods
    def display(self):
        TRIANGLE_SHAPE = (-10, 0, 10, 0, 0, 20)
        CRASH_POINT_ANGLE = 45
        POINTS = 9

        noStroke()
        fill(*self._YELLOW)
        translate(self._x*self._SQUARE_SIZE+self._OFFSET,
                  self._y*self._SQUARE_SIZE+self._OFFSET)

        # Draw first point
        triangle(*TRIANGLE_SHAPE)
        # Draw remaining points
        for _ in range(1, POINTS):
            rotate(radians(CRASH_POINT_ANGLE))
            triangle(*TRIANGLE_SHAPE)
        # Undo translation so subsequent drawn elements
        # are un-translated
        translate(-(self._x*self._SQUARE_SIZE+self._OFFSET),
                  -(self._y*self._SQUARE_SIZE+self._OFFSET))
