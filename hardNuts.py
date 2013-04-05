# determinism vs stochasticism - help!
import random

# fcn no 1. - it's stochastic.  Why?
mylist = []
for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print mylist

# fcns A and B - both deterministic.  Why?
# A
mylist = []
for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print mylist

# B
mylist = []
random.seed(0)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print mylist


def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp


def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1


# newSort will always make more, never fewer inserts than selSort - why?

def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26

# note that this is a better hash fcn than, say, hashing based on the first letter of a word - 
# b/c words beginning with a given letter are unevenly distributed, and in hashing we want
# to aim for even distribution.  This function makes use of modular arithmetic to sum the
# char varlues of every word, divide it by 26 - which yields a sort of average 'value' for
# each word given the baseline shared by all of 26 letters



def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    ***
    Write helper functions as appropriate. If you wish to use insertNewlines
    as a wrapper function that makes an appropriate call to a recursive function,
    please name your recursive helper function insertNewlinesRec so it can be properly
    graded by our automatic grader. lineLength is not the maximum number of characters in
    the line. It is the length after which the next word should be wrapped to the next line.
    Make sure that if a space occurs on the index of the desired line length, the next word
    is wrapped to the next line.
    ***
    """
    ### TODO!  could not get this...
