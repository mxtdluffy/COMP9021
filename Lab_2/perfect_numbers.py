# Written by Di Peng for COMP9021

'''
A number is perfect if it is equal to the sum of its divisors, itself excluded.
For instance, the divisors of 28 distinct from 28 are 1, 2, 4, 7 and 14, and
1+2+4+7+14=28, hence 28 is perfect.

The program prompts the user for an integer N. If the input is incorrect then
the program outputs an error message and exits. Otherwise the program outputs
all perfect numbers at most equal to N. Implement a naive solution, of
quadratic complexity, so that can deal with small values of N only. 
'''

import sys

# This function is used to decomposite the number into a set
def decomposition(s, x):
    if x % 2 == 0:
        x //= 2
        s.add(2)
    elif x % 3 == 0:
        x //= 3
        s.add(3)
    elif x % 5 == 0:
        x //= 5
        s.add(5)
    else:
        return s
    s.add(x)
    decomposition(s, x)

# This function is used to add the rest of number into the set
def getRest(s, x):
    s_reminder = set()
    for i in s:
        s_reminder.add(x//i)
    s_reminder.remove(x)
    s.update(s_reminder)
    return s

# Judge whether x is perfect number
def IsPerfectNum(x):
    s = set([1])
    origin_x = x
    decomposition(s, x)
    getRest(s, x)
    if sum(s) == origin_x:
        return True
    else:
        return False

try:
    N = int(input('Input an integer: '))
    if N <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
for i in range (2, N+1):
    if IsPerfectNum(i):
        print(i,'is a perfect number.') 
