
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)               
    word_list = list(word)
    result_str = ''
    if len(list(word_list)) < 2:
        return word
    for i in range(1, len(word_list), 1):
        if word_list[i] is not word_list[i-1]:
            result_str += word_list[i-1]
    if list(result_str)[-1] is not word_list[-1]:
        result_str += word_list[-1]

    '''
    if len(word)!=0:
        s = word[0]
    else:
        s = ''
    for i in range(1, len(word)):
        if word[i] is not word[i-1]:
            s+=word[i]
    '''
    return result_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
