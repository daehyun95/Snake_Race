import random
from apple import Apple
from snake import Snake
from crash import Crash
from ai import AI


# In order to use contemporary setters in Python 2,
# It's necessary to extend the "object" class. This
# is not necessary in Python 3.
class GameController(object):
    """
    Game Controller class
    """
    def __init__(self, field, gui_controls):
        """
        Initialize game controller
        (Number, Number) GUI_Controls --> GameController
        """
        self.SQUARE_SIZE = 20
        # Attribute names starting with underscores indicate
        # private attributes that should not be accessed
        # outside of the class. We provide necessary access
        # using getters (in "@property" syntax in Python)
        # below.
        self._pix_w = field[0]
        self._pix_h = field[1]
        self._w = self._pix_w//self.SQUARE_SIZE
        self._h = self._pix_h//self.SQUARE_SIZE
        self._deadly_points = set()
        self.set_apple()
        self._playing = True
        self._speed_control = 10
        self._counter = 0
        self._ai_control = AI(self)
        self._human_snake = Snake(self, 'Human', gui_controls)
        self._ai_snake = Snake(self, 'AI', self._ai_control)
        self._allowKeyPress = True

    # Public methods
    # Methods named without an underscore are available
    # to be called from outside the class.
    def update(self):
        """
        Update all game elements
        None --> None
        """
        do_move = not self._counter % self._speed_control
        self._ai_control.update()
        self._ai_snake.update(do_move)
        self._human_snake.update(do_move)
        self._counter += 1
        self._apple.display()

    def set_apple(self):
        """
        Set apple's position
        None --> None
        """
        apple_coords = self._random_coords()
        while apple_coords in self._deadly_points:
            apple_coords = self._random_coords()
        self._apple = Apple(*apple_coords)

    def end_game(self, winner=None, loser=None,
                 event=None, location=None):
        """
        Handle end of game conditions
        Snake? String? (Number, Number)?--> None
        """
        if loser == self._human_snake or winner == self._ai_snake:
            self._winner = self._ai_snake
            self._loser = self._human_snake
        else:
            self._winner = self._human_snake
            self._loser = self._ai_snake

        self._end_event = event
        self._end_location = location
        self._playing = False

    def end_text(self):
        """
        Display game over text
        None --> None
        """
        WHITE = 1
        FONT_SIZE = 50
        VERT_MID = self._pix_h/2
        HORIZ_MID = self._pix_w/2
        VERT_OFFSET = 50

        # Indicate location of game-ending event
        if self._end_location:
            Crash(*self._end_location).display()

        fill(WHITE)
        textSize(FONT_SIZE)
        textAlign(CENTER)

        if self._end_event == 'Collision':
            # In case of a head-on collision
            if self._same_loc(self._human_snake.body[0],
                              self._ai_snake.body[0]):
                text("Head-on Collision!", HORIZ_MID, VERT_MID)
                # If snake are the same length, it's  tie
                if len(self._ai_snake.body) == len(self._human_snake.body):
                    text("TIE",
                         HORIZ_MID, VERT_MID+VERT_OFFSET)
                else:
                    # Otherwise, the winner is the longest snake
                    winner = max([self._ai_snake, self._human_snake],
                                 key=lambda x: len(x.body)).player
                    text(winner + " wins!",
                         HORIZ_MID, VERT_MID+VERT_OFFSET)
            else:
                # Ordinary collision case
                text(self._winner.player + " wins!",
                     HORIZ_MID, VERT_MID)
                text(self._loser.player + " crashed!",
                     HORIZ_MID, VERT_MID+VERT_OFFSET)
        # Attrition case
        elif self._end_event == 'Attrition':
            text(self._winner.player + " wins!",
                 HORIZ_MID, VERT_MID)
            text(self._loser.player + " starved!",
                 HORIZ_MID, VERT_MID+VERT_OFFSET)

    def set_deadly_points(self, deadly_points):
        """
        Set deadly points from a collection of
        coordinates
        [(Number, Number)] --> None
        """
        for dp in deadly_points:
            self._deadly_points.add(dp)

    def add_deadly_point(self, deadly_point):
        """
        Add single deadly point to collection
        (Number, Number) --> None
        """
        self._deadly_points.add(deadly_point)

    def remove_deadly_point(self, deadly_point):
        """
        Remove single deadly point from collection
        (Number, Number) --> None
        """
        if deadly_point in self._deadly_points:
            self._deadly_points.remove(deadly_point)

    def apple_eat(self, snake):
        """
        Handle an apple eat event
        Snake --> None
        """
        if snake == self._human_snake:
            eater = self._human_snake
            other = self._ai_snake
        else:
            eater = self._ai_snake
            other = self._human_snake
        # snake that eats the apple grow
        # Other snake that didn't eats the apple shrink
        eater.grow()
        (done, last_loc) = other.shrink()
        if done:
            self.end_game(
                winner=eater,
                loser=other,
                event='Attrition',
                location=last_loc
            )

    # Private methods
    # Methods intended for use only in this class
    # are conventionally named with an underscore
    # at the beginning
    def _random_coords(self):
        """
        Return random coordinates
        None --> (Number, Number)
        """
        return (random.randint(0, self._w-1), random.randint(0, self._h-1))

    def _same_loc(self, sq1, sq2):
        """
        Determine whether two snake squares are
        in the same location
        SnakeSquare SnakeSquare --> Boolean
        """
        return (sq1.x, sq1.y) == (sq2.x, sq2.y)

# Getters and setters (aka accesssors/mutators).
# These are the values that other classes may need to use from
# this class. This is Python's way of enforcing
# encapsulation, since it does not support truly private attributes.
# Python getters and setters conventionally use the @property syntax,
# with the setter/getter having the same name as the attribute but
# without the leading underscore.

    @property
    def h(self):
        """
        Getter for h value
        None --> Number
        """
        return self._h

    @property
    def w(self):
        """
        Getter for w value
        None --> Number
        """
        return self._w

    @property
    def playing(self):
        """
        Getter for playing value
        None --> Boolean
        """
        return self._playing

    @property
    def deadly_points(self):
        """
        Getter for deadly points
        None --> [Number]
        """
        return self._deadly_points

    @property
    def apple(self):
        """
        Getter for apple
        None --> Apple
        """
        return self._apple

    @property
    def apple_location(self):
        """
        Getter for location of the apple
        None --> (Number, Number)
        """
        return (self._apple.x, self._apple.y)

    @property
    def allowKeyPress(self):
        """
        Getter for allowKeyPress
        None --> Boolean
        """
        return self._allowKeyPress

    # Setter decorator. @property with the same
    # name must be defined above.
    @allowKeyPress.setter
    def allowKeyPress(self, value):
        """
        Setter for allowKeyPress
        Boolean --> None
        """
        self._allowKeyPress = value
