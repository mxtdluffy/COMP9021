# Written by Di Peng

'''
Write a program span.py that prompts the user for a seed for the random number
generator, and for a strictly positive number, nb_of_elements, generates a list
of nb_of_elements random integers between 0 and 99, prints out the list,
computes the difference between the largest and smallest values in the list
without using the builtins min() and max(), prints it out, and check that the
result is correct using the builtins. 
'''

import random

try:
    arg_for_seed = (int)(input('Input a seed for the random number generator:'))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = (int)(input('How many elements do you want to generate:'))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# Generates a list of nb_of_elements random integers between 0 and 99
random.seed(arg_for_seed)
L = [random.randint(0,99) for _ in range(nb_of_elements)]
print('\nThe list is:', L)
max_element = 0
min_element = L[0]
for e in L:
    if e > max_element:
        max_element = e
    if e < min_element:
        min_element = e
print('\nThe maximum difference between largest and smallest values in this list is:', max_element - min_element)
print('Confirming with builtin operation:', max(L) - min(L))
