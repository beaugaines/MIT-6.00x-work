# more palindromes!

import unittest

def pal_1(s):
    """
    (str) -> bool
    Return True if an only if s is a palindrome
    pal_1('noon')  ->  True
    pal_1('fugue')  -> False
    """
    return reverse(s) == s
  

def pal_2(s):
    """
    (str) -> bool
    Return True if an only if s is a palindrome
    pal_1('noon')  ->  True
    pal_1('fugue')  -> False
    """
    if type(s) != str:
        raise ValueError('Must enter a string.')
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    divisor = len(s)//2
    if divisor % 2 == 1:
        return s[:divisor] == s[divisor+1:]
    else:
        return s[:divisor] == s[divisor:]

      

def reverse(s):
    """
    (str) -> str
    Return a reversed version of s
    >>> pal_1('hello')
    'olleh'
    >>> pal_1('a')
    'a'
    """

    rev = ''
    # for each char in s, add each char to the beginning of rev
    for c in s:
        rev = c + rev
    return rev

# tests!

def test(got,expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' FAIL '
    print "{0} got: {1}, expected {2}".format(prefix, repr(got), repr(expected))




# test pal_1
print 'test pal_1'
print '----------'
test(pal_1('bob'), True)
test(pal_1('a'), True)
test(pal_1('fugue'), False)

# test pal_2
print 'test pal_2'
print '----------'
test(pal_2('bob'), True)
test(pal_2('a'), True)
test(pal_2('fugue'), False)
test(pal_2(''), False)