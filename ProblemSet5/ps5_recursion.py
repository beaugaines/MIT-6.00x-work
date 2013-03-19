# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.

    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    # base case of empty string
    if x == "":
        return True

    # case of x being longer than word
    if len(x) > len(word):
        return False

    # case of x and word being identical
    if x == word:
        return True

    # check to see if first chars of x and word are same
    elif(x[0] == word[0]):
        return x_ian(x[1:], word[1:])

    # otherwise check the next character in word for a match
    else:
        return x_ian(x, word[1:])


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """

    wordList = text.split()
    textLength = len(text)

    textCopy = text[:]
    newString = ''
    tempString = ''

    while len(wordList) > 0:
        tempWord = wordList.unshift()
        while len(tempString) < lineLength:
            newString += tempWord + ' '
        newString += tempString + '.\n'
    return newString






