# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


lettersGuessed = []
letters = list(string.ascii_lowercase)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return(sorted(list(set(secretWord))) == sorted(list(lettersGuessed)))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    word = list(secretWord)
    word = map(lambda x: x if x in lettersGuessed else '_', word)
    return ''.join(word)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for c in lettersGuessed:
        if c in letters:
            letters.remove(c)
    return(''.join(letters))
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to Hangman!\n")
    print("The secret word contains " + str(len(secretWord)) + " words.\n")
    numGuesses = 0
    lettersGuessed = []
    # loop till the right word is guessed!  They'll get it eventually!

    while numGuesses < 8:
        guess = raw_input("Guess a letter: \n")
        guess = guess.lower()
        if guess in letters:
            letters.remove(guess)

        if guess in secretWord:
            if guess in lettersGuessed:
                print('You already guessed that.')
                pass
            else:
                print('You guessed a letter!\n\n')
                lettersGuessed.append(guess)
                if isWordGuessed(secretWord, lettersGuessed):
                    print("You got the word! Here it is: " +
                        getGuessedWord(secretWord, lettersGuessed) + '\n')
        else:
            print('That\'s not in the word')
            numGuesses += 1
        print("You have " + str((8 - numGuesses)) + ' remaining.\n')
        print("Here's what you guessed so far " + \
            getGuessedWord(secretWord, lettersGuessed) + '\n')

        print('The letters you have not guessed fo far are: ' + \
            getAvailableLetters(lettersGuessed) + '\n')

    print('You lose.  The word is ' + secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
