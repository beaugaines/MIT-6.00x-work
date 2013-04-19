import pylab


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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    VOWELS = 'aeiou'
    freq = {}
    vowel_proportions = []
    for w in wordList:
        num_vowels = 0
        for c in w:
            if c in VOWELS:
                num_vowels += 1
        vowel_proportions.append(num_vowels/float(len(w)))
    # mean = sum(total)/float(len(total))
    # plot histogram with pyab
    pylab.hist(vowel_proportions, numBins)
    pylab.xlabel('Proportion of vowels')
    pylab.ylabel('Number of occurrences')
    # return min and max vals on x axis
    xmin, xmax = pylab.xlim()
    # likewise for y axis
    ymin, ymax = pylab.ylim()
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
