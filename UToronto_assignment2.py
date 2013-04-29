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
        return("{0} at ({1}, {2}) ate {3} sprouts.\n".format(self.rat,
                 str(self.row), str(self.col), str(self.num_sprouts_eaten))) 

class Maze:
    """ A 2D maze. 
    (Maze, list of list of str, Rat, Rat) -> NoneType
    """

    def __init__(self, maze, rat_1, rat_2, num_sprouts_left):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        '''(Maze, int, int) -> bool'''
        return(self.maze[row][col] == '#')

    def get_character(self, row, col):
        '''(Maze, int, int) -> str'''
        return(self.maze[row][col])

    def move(self, rat, row, col):
        '''(Maze, Rat, int, int) -> bool'''
        new_row, new_col = self.rat.row + row, self.rat.col + col
        new_pos = self.maze[new_row][new_col]
        # eat a sprout if it's there for the eating
        if new_pos == '@':
            rat.eat_sprout()
        # if new position is not a wall, set new position of rat
        if new_pos != '#':
            rat.row, rat.col = new_row, new_col
            return True
        # it's a wall - no luck, rat
        return False


    def __str__(self):
        '''(Maze) -> str'''
        res = '\n'.join(''.join([str(c) for c in list] for list in self.maze))
        res += self.rat_1.str() + self.rat_2.str()
        return res


