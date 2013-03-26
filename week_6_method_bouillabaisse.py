
# a gloriously hideous regex I came up with - part of 'Dive into Python' - but 
# I love regexes so much I assembled it on my own

hideousRegex = """
^
\(?                # match a possible opening bracket for area code 
(\d{3})            # area code at beginning of string
\)?                # match a possible closing bracket
\D*                # one or more 'non-word' character - e.g. a hyphen, a space
(\d{3})            # trunk code
\D*                # one or more 'non-word' chars
(\d{4})            # last 4 digits
\D*                # more non-words
(\d*)?             # maybe an extension of one or more digits
$
"""

# first (admittedly underwhelming) class written from scratch!

class Queue(object):
    
    ''' a standard queue that stores elements in a list
    and returns them in FIFO fashion. '''
    
    def __init__(self):
        ''' store the junk in a regular list, inherited from object '''
        self.storage = []
        
    
    def insert(self, e):
        ''' get thee to the end of the line, e '''
        self.storage.append(e)
        
    def remove(self):
        ''' hack to emulate Perl's shift method.  Why not just have
        a shift method in Python? '''
        try:
            # res = self.storage[0]
            # del self.storage[0]
            # return res
            ''' ok - learned you can give an index argument to pop... '''
            return self.storage.pop(0)
        except:
            raise ValueError()


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