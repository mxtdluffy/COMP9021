

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    word_list = list(word)
    record_list = [word_list[0]]
    record_word = word_list[0]
    for i in range(0, len(word_list)-1):
        if ord(word_list[i]) + 1 == ord(word_list[i+1]):
            record_word += word_list[i+1]
            if i == len(word_list) - 2:
                record_list.append(record_word)
        else:
            record_list.append(record_word)
            record_word = word_list[i+1]
    for i in record_list:
        if desired_length < len(list(i)):
            desired_length = len(list(i))
            desired_substring = i
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
