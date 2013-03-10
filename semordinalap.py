def semordnilapWrapper(str1, str2):
    ''' Takes two words and returns whether or not
    they are semordnilaps of each other.
    Ex.  nametag / gateman
        dog / god
        live / evil
        desserts / stressed
    '''

    if len(str1) == 1 or len(str2) == 1:
        return False
    elif str1 == str2:
        return False
    else:
        return semordnilap(str1, str2)

def semordnilap(str1, str2):
    # manage case of strings of inequal length
    if len(str1) != len(str2):
        return False
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return True
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])



semordnilapWrapper('dog', 'god')

semordnilap('dog', 'god')

