class Location(object):

    """
    (int, int) -> str

    Takes two integers describing the initial x and y coordinates of a drunken farmer
    and returns a string describing his location after stumbling around for awhile
    l = Location(5,6)
    print l  -> (5,6)
    """

    def __init__(self):
        """x and y are floats"""
        self.x = x
        self.y = y


    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y)

