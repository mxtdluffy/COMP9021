'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''
import copy

def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''    
    dictionary = 'dictionary.txt'
    solutions = []
    dictionary_set = set()
    # Insert your code here
    with open(dictionary) as dictionary_file:
        for line in dictionary_file:
            dictionary_set.add(line.replace('\n',''))

    #TODO: sort the input letters
    #check whether every string is in list

    letters_list = list()
    for i in dictionary_set:
        if len(i) > len(letters):
            continue
        if set(letters) & set(i) == set(i):
            second_word = set(letters) - set(i)
            for j in dictionary_set:
                if len(j) > len(second_word):
                    continue
                if set(second_word) & set(j) == set(j):
                    words = list(i + j)
                    words.sort()
                    letters_sorted = list(letters)
                    letters_sorted.sort()
                    if words == letters_sorted:
                        word_list = list()
                        word_list.append(i)
                        word_list.append(j)
                        word_list.sort()
                        x, y = word_list
                        if (x,y) not in solutions:
                            solutions.append((x, y))
    
    solutions.sort()

    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
