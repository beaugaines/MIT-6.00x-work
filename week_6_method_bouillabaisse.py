
# hashSet fcn - building on earlier intSet class

class hashSet(object):

    '''
    hacked together class implementing much of the fcnality of Python native
    hash fcn i.e. dictionaries - but in much less efficient fashion
    '''

    def __init__(self, numBuckets):
        '''
        numBuckets:  int.  The number of buckets this hash set will have.  Raises
        ValueError if this value is not an integer, or if it is not greater
        than zero.
        
        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if type(numBuckets) != int or numBuckets <= 0:
            raise ValueError
        else:
            hashSet = []
            for i in range(0, numBuckets):
                hashSet.append([])

    def hashValue(self, e):
        '''
        e: an integer
        
        returns: a hash value for e, which is e mod the number 'o buckets in
        this hash set.  Raise ValueError if e is not an int.
        '''
        if type(e) != int:
            raise ValueError
        else:
            return e % len(hashSet)


    def getNumBuckets(self):
        '''
        returns number of buckets in your sorry little hash
        '''
        return len(self.hashSet)


    def member(self, e):
        '''
        e: an integer
    
        returns: True if e is in self, False otherwise
        Raise ValueError if e not an integer
        '''
        if type(e) != int:
            raise ValueError
        else:
            for bucket in self.hashSet:
                return e in bucket

    def insert(self, e):
        '''
        e: an integer
        
        inserts e into appropriate hash bucket.  Raises ValueError
        if e is not an integer.
        '''
        if self.member(e):
            return
        else:
            self.hashSet[self.hashValue(e)].append(e)


    def remove(self, e):
        '''
        e: an integer
        
        removes e from self.  Raises ValueError if e is not in
        self or if e is not an int.
        '''
        if not self.member(e) or type(e) != int:
            return ValueError
        else:
            self.hashSet[self.hashValue(e)].remove(e)

    def __str__(self):
        '''
        returns the hash itself rather than some vague and useless
        < function at 90993j3ijoc > gibberish
        '''
        return str(self.hashSet)

# primeGen generator fcn

def primeGen():
    ''' generator function that yields an prime sequence of arbitrary length  '''

    primes = []
    x = 1
    while True:
        x += 1
        # nifty trick here - since primes is empty on the first run
        # through this yields true for 2
        if all(x % m != 0 for m in primes):
            primes.append(x)
            yield x


# a gloriously hideous regex I came up with - part of 'Dive into Python' - but 
# I love regexes so much I assembled it on my own. Refactored to *not* match beginning
# of string - so any superfluous verbiage before the number will be ignored

hideousRegex = """
                   # don't match beginning of string, number can start anywhere
\(?                # match a possible opening bracket for area code 
(\d{3})            # area code at beginning of string
\)?                # match a possible closing bracket
\D*                # one or more 'non-word' character - e.g. a hyphen, a space
(\d{3})            # trunk of number - 3 digits
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