import string

# our highly useful English to French dictionary

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'eats':'mange', 'drinks':'boit', 'John':'Jean', 'friends':'amis', 'and':'et', 'of':'du', 'red':'rouge'}

# make the reverse dict
FtoE = {}
for (k,v) in EtoF.items():
    FtoE[v] = k

dicts = {'English to French': EtoF, 'French to English': FtoE}


# basic translate fcn

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
  # must have final return to return empty strings
    return word



def translate(phrase, dicts, direction):
    import string
    letters = string.ascii_letters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        
        # elminate non-word characters
        if c in letters:
            word = word + c
        else:
            
            # add to translation the translated word plus 'c' - which b/c
            # we are in the else clause must be whitespace or punctuation
            translation += translateWord(word, dictionary) + c
            
            # reset word to blank string for next time through loop
            word = ''
            
    # out of loop now - return the final translation
    return translation + ' ' + translateWord(word, dictionary)


# take a test drive!

print translate('John drinks good red wine, and eats bread.', dicts, 'English to French')

print translate('Jean boit du vin rouge.', dicts, 'French to English')


# output
Jean boit "good" rouge vin, et mange pain. 
John drinks of wine red. 
[Finished in 0.1s]