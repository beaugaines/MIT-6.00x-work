# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. 
    (Rat, str, int, int) -> NoneTye
    """

    def __init__(self, rat, row, col):
        self.rat = rat
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        '''(Rat, int, int) -> Nonetype'''
        self.row = row
        self.col = col

    def eat_sprout(self):
        '''(Rat) -> NoneType'''
        self.num_sprouts_eaten += 1

    def __str__(self):
        '''(Rat) -> str'''
        return("{0} at ({1}, {2}) ate {3} sprouts".format(self.rat,
                 self,row, self.col, self.num_sprouts_eaten) 

class Maze:
    """ A 2D maze. 
    (Maze, list of list of str, Rat, Rat) -> NoneType
    """

    def __init__(self, maze, rat_1, rat_2, num_sprouts_left):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = num_sprouts_left

    def is_wall(self):
        pass

    def get_character(self):
        pass

    def move(self, rat):
        pass

    def __str__(self):
        pass
