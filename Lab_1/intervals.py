# Written by Di Peng

'''
Write a program named intervals.py that prompts the user for a strictly
positive integer, nb_of_elements, generates a list of nb_of_elements random
integers between 0 and 19, prints out the list, computes the number of
elements strictly less than 5, 10, 15 and 20, and prints those out.
'''

from random import seed, randrange
import sys

try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

# Generates a list of nb_of_elements random integers between 0 and 19
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThis list is:', L)
print()
remainders_intervals = [0] * 4

# - remainders_intervals[0] to record the number of elements between 0 to 4
# - remainders_intervals[1] to record the number of elements between 5 to 9
# - remainders_intervals[2] to record the number of elements between 10 to 14
# - remainders_intervals[3] to record the number of elements between 15 to 19
# if e is 0, it cannot be divisioned
for e in L:
    if e == 0:
        remainders_intervals[0] += 1
    else:
        remainders_intervals[int(e / 5)] += 1

for i in range(4):
    if remainders_intervals[i] == 0:
        print('There is no element', end = ' ')
    elif remainders_intervals[i] == 1:
        print('There is 1 element', end = ' ')
    else:
        print(f'There are {remainders_intervals[i]} elements', end = ' ')
    print(f'between {i*5} and {i*5+4}.')
