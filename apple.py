class Apple:
    """
    The apple
    """
    def __init__(self, x, y):
        """
        Initialize an apple at coordinates
        Number, Number --> None
        """
        self._x = x
        self._y = y
        self._SIZE = 20
        self._OFFSET = 10
        self._GREEN = (0, 1, 0)
        self._BLACK = 0
        self._WHITE = 1
        self._LINE_WEIGHT = 2

    def display(self):
        strokeWeight(self._LINE_WEIGHT)
        stroke(self._BLACK)
        fill(*self._GREEN)

        # Draw apple circle
        ellipse(
            self._x*self._SIZE+self._OFFSET,
            self._y*self._SIZE+self._OFFSET,
            self._SIZE, self._SIZE
            )
        fill(self._WHITE)

        # Draw shiny spot on apple
        noStroke()
        QUARTER_ADJUST = 2.5
        SHINE_ADJUST = 1.25
        ellipse(
            self._x*self._SIZE+self._OFFSET/SHINE_ADJUST,
            self._y*self._SIZE+self._OFFSET/SHINE_ADJUST,
            self._SIZE/QUARTER_ADJUST,
            self._SIZE/QUARTER_ADJUST)

        # Draw apple stem
        noFill()
        stroke(0)
        STEM_ADJUST_1 = 1.35
        STEM_ADJUST_2 = 1.75
        arc(
            self._x*self._SIZE+self._OFFSET*STEM_ADJUST_1,
            self._y*self._SIZE+self._OFFSET/STEM_ADJUST_2,
            self._SIZE/QUARTER_ADJUST,
            self._SIZE/QUARTER_ADJUST,
            HALF_PI, PI)
        STEM_ADJUST_3 = 1.4
        arc(
            self._x*self._SIZE+self._OFFSET*STEM_ADJUST_3,
            self._y*self._SIZE+self._OFFSET,
            self._SIZE/QUARTER_ADJUST,
            self._SIZE/QUARTER_ADJUST,
            PI+QUARTER_PI, PI+HALF_PI)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
