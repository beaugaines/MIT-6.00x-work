def getGuessedWord(secretWord, lettersGuessed):
    if secretWord != "":
        if secretWord[0] in lettersGuessed:
            # guessed = guessed + 1
            print secretWord[0],
            return getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            print '_',
            return getGuessedWord(secretWord[1:], lettersGuessed)
    return ''