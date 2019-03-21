# Written by Di Peng

'''
Write a program named mean_median_standard_deviation.py that prompts the user
for a strictly positive integer, nb_of_elements, generates a list of
nb_of_elements random integers between - 50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways, that
is, using or not the functions from the statistics module, and prints them out.
'''

from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys

# the function is used to swap two numbers in a list
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

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

seed(arg_for_seed)
L = [randint(-50, 50) for _ in range(nb_of_elements)]
print('\nThe list is:', L)

# sort the L from minimum to maximum
for i in range(nb_of_elements):
    for j in range(nb_of_elements):
        if L[i] < L[j]:
            swap(L, i, j)
elements_total = 0

# calculate the mean of all elements
for e in L:
    elements_total += e
mean_value = elements_total / nb_of_elements


# calculate the median of all elements
median_value = 0
if nb_of_elements % 2 == 0:
    median_value = L[int(nb_of_elements / 2)] + L[int(nb_of_elements / 2) - 1]
    median_value /= 2
else:
    median_value = L[int(nb_of_elements / 2)]

# calculate the standard deviation of all elements
standard_deviation_total = 0.0
for e in L:
    standard_deviation_total += pow(e - mean_value, 2)
standard_deviation_total /= nb_of_elements
standard_deviation_value = sqrt(standard_deviation_total)
print(f'\nThe mean is {mean_value:.2f}.')
print(f'The median is {median_value:.2f}.')
print(f'The standard deviation is {standard_deviation_value:.2f}.')

# Using the functions from the statistics module
print('\nConfirming with functions from the statistics module:')
mean_value = mean(L)
median_value = median(L)
standard_deviation_value = pstdev(L)
print(f'The mean is {mean_value:.2f}.')
print(f'The median is {median_value:.2f}.')
print(f'The standard deviation is {standard_deviation_value:.2f}.')

