
# more palindromes!


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
    n = len(s)
    if n == 0:
        return False
    if n == 1:
        return True
    return s[:n // 2] == reverse(s[(n - n //2):])


def pal_3(s):
    """
    (str) -> bool
    Return True if an only if s is a palindrome
    pal_1('noon')  ->  True
    pal_1('fugue')  -> False
    """
    if len(s) == 0:
        return False
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return j <= i

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
test(pal_2('dented'), False)


# test pal_3
print 'test pal_3'
print '----------'
test(pal_3('bob'), True)
test(pal_3('a'), True)
test(pal_3('fugue'), False)
test(pal_3(''), False)
test(pal_3('dented'), False)

