
class WordplayStr(str):
    ''' a string that can repot whether it has interesting properties '''

    def same_start_and_end(self):
        ''' (WordplayStr) -> bool

        Precondition: len(self) != 0

        Return whether self starts and ends with same letter

        >>> s = WordplayStr('abracadabra')
        >>> s.same_start_and_end
        True
        >>> s = WordplayStr('canoe')
        >>> s.same_start_and_end
        False
        '''
        return self[0] == self[-1]


if __name__ == 'main':
    import doctest
    doctest.testmod()