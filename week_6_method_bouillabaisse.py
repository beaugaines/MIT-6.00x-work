# custom intersect and len methods

class intSet(object):

    def __init__(self):
        self.vals = []

        def intersect(self, other):
        ''' Returns a set consisting of the intersecting elements
        of two distinct sets.  Returns an empty set if there is
        no intersection '''
        res = []
        for e in self.vals:
            if e in other.vals:
                res.append(e)
        if len(res) == 0:
            return '{}'
        else:
            return '{' + ','.join([str(e) for e in res]) + '}'
        
    def __len__(self):
        return len(self.vals)


# my __eq__ and __repr__ methods

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __repr__(self):
        return 'Coordinate(%i, %i)' % (self.x, self.y)