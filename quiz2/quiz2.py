# Written by Di Peng and Eric Martin for COMP9021



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

def redFraction(numerator, denominator):
    gcd_number = gcd(numerator, denominator)
    return numerator//gcd_number, denominator//gcd_number 

def getPrimeFactors(number):
    i = 2
    dic_prime_factors = {}
    while i <= number:
        if number % i == 0:
            number = number // i
            if i in dic_prime_factors.keys():
                dic_prime_factors[i] += 1
            else:
                dic_prime_factors.setdefault(i, 1)
        else:
            i += 1
    return dic_prime_factors

dic_reminder = {}
most_complex_fraction_reminder = " "
simplest_fraction_reminder = " " * 20
for origin_numerator in L:
    for origin_denominator in L:
        if origin_numerator/origin_denominator > 1:
            continue
        else:
            change_numerator, change_denominator = redFraction(origin_numerator, origin_denominator)
            dic_key = str(change_numerator) + '' + str(change_denominator)
            dic_reminder.setdefault(redFraction(origin_numerator, origin_denominator), change_numerator/change_denominator)
            # Calculate the size of simplest fraction
            if len(dic_key) < len(simplest_fraction_reminder):
                simplest_fraction_reminder = dic_key
                size_of_simplest_fraction = len(dic_key)
            # Calculate the size of most complex fraction
            if len(dic_key) > len(most_complex_fraction_reminder):
                most_complex_fraction_reminder = dic_key
                size_of_most_complex_fraction = len(dic_key)

string_of_fraction = None
for x,y in sorted(dic_reminder.items(), key=lambda item: item[1]):
    first_number, second_number = x
    string_of_fraction = str(first_number)+str(second_number)
    if len(string_of_fraction) == size_of_simplest_fraction:
        simplest_fractions.append((first_number, second_number))
    if len(string_of_fraction) == size_of_most_complex_fraction:
        most_complex_fractions.append((first_number, second_number))

most_complex_fractions.reverse()
prime_factors = []
for x,y in most_complex_fractions:
    prime_factors.append(getPrimeFactors(y))

for dic_prime_factors in prime_factors:
    try:
        x, y = max(dic_prime_factors.items(), key=lambda item:item[1])
        if multiplicity_of_largest_prime_factor < y:
            multiplicity_of_largest_prime_factor = y
    except ValueError:
        multiplicity_of_largest_prime_factor = 0
        largest_prime_factors = []
        
for dic_prime_factors in prime_factors:
    for key, value in dic_prime_factors.items():
        if value == multiplicity_of_largest_prime_factor:
            if key not in largest_prime_factors:
                largest_prime_factors.append(key)
largest_prime_factors = sorted(largest_prime_factors)

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
        
        
