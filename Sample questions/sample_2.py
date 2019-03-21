
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    # Insert your code here
    print('Here are your banknotes:')
    notes_dic = dict()
    '''
    while N != 0:
        record = 0
        amount = 0
        for i in range(len(banknote_values)):
            if N < banknote_values[i]:
                record = banknote_values[i-1]
                break
            if i == len(banknote_values) - 1:
                record = banknote_values[-1]
        amount = int(N/record)
        N = N % record
        notes_dic.setdefault(record,amount)

    for i in range(len(banknote_values)):
        if banknote_values[i] in notes_dic.keys():
            print(f'${banknote_values[i]}: {notes_dic[banknote_values[i]]}')
    '''
    
    for i in range(len(banknote_values)-1,-1,-1):
        count = N // banknote_values[i]
        notes_dic.setdefault(banknote_values[i],count)
        N = N % banknote_values[i]
        
    for i in range(len(banknote_values)):
        if notes_dic[banknote_values[i]] > 0:
            print(f'${banknote_values[i]}: {notes_dic[banknote_values[i]]}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
