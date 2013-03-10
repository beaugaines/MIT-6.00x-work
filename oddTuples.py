def oddTuples(tup):
    '''Take a tuple as input and return
    a new tuple as output, where every OTHER
    element of the input tuple is copied, starting
    with the first one.'''

    newTup = ()

    for n in range(len(tup)):
        if n % 2 == 0:
            newTup += (tup[n],)
    return newTup
