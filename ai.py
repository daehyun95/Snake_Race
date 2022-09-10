from snake_controller import SnakeController

# These constant assignments are redundant and
# already provide by Processing, however
# providing them here makes it possible to run
# tests in Pytest on functions using them.
UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


class AI(SnakeController):
    """
    AI Snake controller class
    """

    def __init__(self, gc):
        """
        Initialize AI
        GameController --> AI
        """
        self._gc = gc

    # Public methods
    def update(self):
        """
        Calculate next move and control the snake
        None --> None
        """
        dir = self._choose_dir()
        self.control_snake(dir)

    # Private methods
    def _choose_dir(self):
        """
        Score directions and return top scored
        direction
        None --> Direction
        """
        directions = [UP, DOWN, LEFT, RIGHT]

        # TODO Problem 2: Integrate AI to choose the direction
        # for the AI snake.

        # The AI should choose the direction that gets it
        # closest to the apple with a preference for open spaces
        # (I.e. it should prefer to move to squares with fewer
        # occupied neighboring squares).

        # All necessary supporting methods have been implemented
        # in this class already. The only modifications you need
        # to make are to this method. Use the methods below to
        # determine the scores and choose the direction
        distances = []
        clear_neighbors = []

        # For each direction from the head of square get the neighbor location
        # With that, get the score of distance to apple and
        # append to the distances list
        # get the score with _clear_score with neighbor_location and
        # append it to the neighbor list
        for dir in directions:
            neighbor_location = self._get_neighbor_coord(dir)
            distances.append(self._apple_distance(neighbor_location))
            clear_neighbors.append(self._clear_score(neighbor_location))

        # Multiply two elements in two different list with same position
        # Add to total_score list
        total_score = []
        for i in range(len(distances)):
            total_score.append(distances[i] * clear_neighbors[i])

        # Each element of list represent the direction
        # choose the max value from the total_score and
        # the position of that will be the direction
        position = total_score.index(max(total_score))
        return directions[position]

    def _get_neighbor_coord(self, neighbor_dir):
        """
        Get neighbor coordinate for direction
        Direction --> (Number, Number)
        """
        x = self._snake.body[0].x
        y = self._snake.body[0].y
        if neighbor_dir == UP:
            return (x, y-1)
        elif neighbor_dir == DOWN:
            return (x, y+1)
        elif neighbor_dir == LEFT:
            return (x-1, y)
        elif neighbor_dir == RIGHT:
            return (x+1, y)

    def _min_dist(self, p1, p2):
        """
        Find the minimum distance between two points
        (Number, Number) (Number, Number) --> Number
        """
        # To find the shortest path between two points
        # We calculate the inner path (within the game frame)
        # and the outer path (going out of the bounds of the
        # frame and wrapping in the other side) and take the
        # minimum of the two.
        p1_x, p1_y = p1
        p2_x, p2_y = p2

        inner_x = p1_x - p2_x
        inner_y = p1_y - p2_y

        outer_x = self._gc.w-(max(p1_x, p2_x)) + min(p1_x, p2_x)
        outer_y = self._gc.h-(max(p1_y, p2_y)) + min(p1_y, p2_y)

        # print("Outer x", outer_x)
        # print("Outer y", outer_y)

        # Pythagorean theorem
        shortest = (min(inner_x, outer_x)**2+min(inner_y, outer_y)**2)**0.5
        return shortest

    def _clear_score(self, coord):
        """
        Generate a weighting score (normalized)
        from the number of unoccupied neighbor squares
        for a coordinate
        (Number, Number) --> Number
        """
        # normalized number of clear neighbor squares
        if coord in self._gc.deadly_points:
            return -1
        else:
            score = 0
            if (coord[0]-1, coord[1]) not in self._gc.deadly_points:
                score += 1
            if (coord[0], coord[1]-1) not in self._gc.deadly_points:
                score += 1
            if (coord[0], coord[1]+1) not in self._gc.deadly_points:
                score += 1
            if (coord[0]+1, coord[1]) not in self._gc.deadly_points:
                score += 1
        NEIGHBOR_COUNT = 4.0
        score = score/NEIGHBOR_COUNT
        return score

    def _apple_distance(self, coords):
        """
        Get the distance score to the apple
        (Number, Number) --> Number
        """
        # Get the distance
        apple_min_dist = self._min_dist(self._gc.apple_location, coords)
        # Return the distance score
        return self._convert_min_to_score(apple_min_dist)

    def _convert_min_to_score(self, min_dist):
        """
        Convert a distance to a score
        Number --> Number
        """
        return ((self._gc.h * self._gc.w) - min_dist)
