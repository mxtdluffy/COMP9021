import sys
from math import sqrt


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    try:
        last_min_n = n
        for i in range(last_min_n, 1, -1):
            if i <= 2:
                largest_prime_strictly_smaller_than_n = 2
                raise ValueError
            for x in range(2, int(sqrt(last_min_n))+1):
                if i % x == 0:
                    break
                if x >= int(sqrt(last_min_n)):
                    largest_prime_strictly_smaller_than_n = i
                    raise ValueError
    except ValueError:
        print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
