# my custom recursive range fcn

def recurRange(x,y,step,storage=[]):    
    storage.append(x)
    if y - x == 1:
        return storage
    else:
        return recurRange(x+step,y,step,storage)


# to build up a frequency hash from a string

freq = {}
for c in string:
    freq[c] = freq.get(c, 0) + 1



# my isPrime fcn

def isPrime(n):
    """ returns True if n is prime, False otherwise """

    # if n is not type int, raise TypeError
    if type(n) != int:
        raise TypeError

    # if n is less or eql to 0, raise ValueError
    if n <= 0:
        raise ValueError


    # otherwise check for primality; testing up to square root of n improves efficiency

    if n == 2:
        return True

    elif n < 2:
        return False

    # iterate over vals from 2 through sqrt(n) to see if there are any divisors

    for div in range(2, int(n**0.5 + 1)):
        if n % div == 0:
            return False

    # exited loop with no clean divisors - so the thing is prime

    return True



