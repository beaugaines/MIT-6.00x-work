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
            self.storage = []
            for i in range(0, numBuckets):
                self.storage.append([])

    def hashValue(self, e):
        '''
        e: an integer
        
        returns: a hash value for e, which is e mod the number 'o buckets in
        this hash set.  Raise ValueError if e is not an int.
        '''
        if type(e) != int:
            raise ValueError
        else:
            return e % len(self.storage)


    def getNumBuckets(self):
        '''
        returns number of buckets in your sorry little hash
        '''
        return len(self.storage)


    def member(self, e):
        '''
        e: an integer
    
        returns: True if e is in self, False otherwise
        Raise ValueError if e not an integer
        '''
        if type(e) != int:
            raise ValueError
        else:
            for bucket in self.storage:
                if e in bucket:
                    return True
                else:
                    continue
            return False

    def insert(self, e):
        '''
        e: an integer
        
        inserts e into appropriate hash bucket.  Raises ValueError
        if e is not an integer.
        '''
        if self.member(e):
            return
        else:
            self.storage[self.hashValue(e)].append(e)


    def remove(self, e):
        '''
        e: an integer
        
        removes e from self.  Raises ValueError if e is not in
        self or if e is not an int.
        '''
        if not self.member(e) or type(e) != int:
            raise ValueError
        else:
            self.storage[self.hashValue(e)].remove(e)

    def __str__(self):
        '''
        returns the hash itself rather than some vague and useless
        < function at 90993j3ijoc > gibberish
        '''
        return str(self.storage)
