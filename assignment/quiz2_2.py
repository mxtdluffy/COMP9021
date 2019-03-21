# Written by *** and Eric Martin for COMP9021



import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE

all_of_fractions = []
from fractions import Fraction
for number_n in L:
    for number_m in L:
        if Fraction(number_n,number_m) < 1:
            all_of_fractions.append(str(Fraction(number_n,number_m)))
        if Fraction(number_n,number_m)   == 1:        # when the numerator and denominator are the same
            all_of_fractions.append('1/1')                   # when the result is 1, 1/1 len=3
all_of_fractions = set(all_of_fractions)
biggest_len = max(all_of_fractions, key = len)        # use set to eliminate the same result
smallest_len = min(all_of_fractions, key = len)        # get max and min len of all result
size_of_most_complex_fraction = len(biggest_len) -1
size_of_simplest_fraction = len(smallest_len)-1


all_smallest_fractions = []                      # put the fraction in list and sorted
for number in all_of_fractions:
    if len(number) == len(smallest_len):
        all_smallest_fractions.append( Fraction(number))
        all_smallest_fractions = sorted(all_smallest_fractions)
        
for number_in_fractions in all_smallest_fractions:
    fractions_group = (number_in_fractions.numerator, number_in_fractions.denominator) 
    simplest_fractions.append(fractions_group)

all_most_complex_fractions = []
for number in all_of_fractions:
    if len(number) == len(biggest_len):
        all_most_complex_fractions.append(Fraction(number))
all_most_complex_fractions = sorted(all_most_complex_fractions,reverse = True)  # True: soretd () passing parameters in decreasing order
                                                                                                                   # Fales: soretd () passing parameters in increasing order    
for number_in_fractions in all_most_complex_fractions:
    fractions_group = (number_in_fractions.numerator, number_in_fractions.denominator) 
    most_complex_fractions.append(fractions_group)
    

for x,y in most_complex_fractions:
    digit = y
    dic_pir_factors = {}
    for i in range(2,digit+1):
        while digit % i == 0:
            #print i,"|",n
            digit = digit // i
            if i in dic_pir_factors.keys():
                dic_pir_factors[i] = dic_pir_factors[i] + 1
            else:
                dic_pir_factors[i] = 1
        if digit == 1: 
            break
    largest_prime_factors.append(dic_pir_factors)
    
multiplicity_of_largest_prime_factor = 0
prime_factors = largest_prime_factors
for dic_pir_factors in prime_factors:
    for i in dic_pir_factors.values():
        if multiplicity_of_largest_prime_factor < i:
            multiplicity_of_largest_prime_factor = i

largest_prime_factors = []
largest_set = set()
for dic_pir_factors in prime_factors:
    for i in dic_pir_factors.keys():
        if dic_pir_factors[i] == multiplicity_of_largest_prime_factor:
            largest_set.add(i)
            
largest_set = sorted(largest_set)
for i in largest_set:
    largest_prime_factors.append(i)
        
print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
