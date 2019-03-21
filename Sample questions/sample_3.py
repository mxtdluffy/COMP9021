'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''


def good_subsequences(word):
    '''
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    word_list = list(word)
    remove_list = list()        
    for i in range(1, len(word_list), 1):
        if word_list[i] is not word_list[i-1]:
            remove_list.append(word_list[i-1])
    if list(remove_list)[-1] is not word_list[-1]:
        remove_list.append(word_list[-1])
    result_list = list()
    result_list.append('')
    if len(remove_list) < 2:
        result_list.append(remove_list[0])
    for i in range(len(remove_list)):
        new_list = [remove_list[x] for x in range(i, len(remove_list), 1)]
        word = remove_list[i]
        if word not in result_list:
            result_list.append(word)
        for x in range(len(new_list)):
            for y in range(x,len(new_list),1):
                if new_list[y] not in list(word):
                    word += new_list[y]
                    if word not in result_list:
                        result_list.append(word)
            word = remove_list[i]
    result_list.sort()
    print(result_list)
    
# Possibly define another function

if __name__ == '__main__':
    import doctest
    doctest.testmod()
