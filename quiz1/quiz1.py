# Written by Di Peng and Eric Martin for COMP9021



import sys
from random import seed, randrange

# Split number to a String list
def splitnumber(number):
    list_of_split = list(str(number))
    return list_of_split

# Calculate the gap between first and last digit
def calfirsttolast(number):
    list_of_number = splitnumber(number)
    return int(list_of_number[0]) - int(list_of_number[-1])

#Calculate the sum of all digits
def sumofdigits(number):
    list_of_number = splitnumber(number)
    sum_of_all_digits = 0
    for i in list_of_number:
        sum_of_all_digits += int(i)
    return sum_of_all_digits

#Calculate the number of distinct digit
def caldistinctdigit(number):
    list_of_number = set(splitnumber(number))
    return len(list_of_number)

#get the first digit of number 
def getfirst(number):
    list_of_split = list(str(number))
    return int(list_of_split[0])

#get the last digit of number 
def getlast(number):
    list_of_split = list(str(number))
    return int(list_of_split[-1])
    
try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

# REPLACE THIS COMMENT WITH YOUR CODE
print('\nx is:', x)
print('L is:', L)

sum_of_digits_in_x = sumofdigits(x)
print(f'\nThe sum of all digits in x is equal to {sum_of_digits_in_x}.')

dic_reminder = {}
for i in L:
    gap_value = calfirsttolast(i)
# if the gap value is greater than 0, first digit is greater than the last digit
# if the gap value is equal to 0, first digit is equal to the last digit
# if the gap value is less than 0, last digit is greater than first digit
    if gap_value > 0:
        first_digit_greater_than_last += 1
    elif gap_value == 0:
        same_first_and_last_digits += 1
    else:
        last_digit_greater_than_first += 1
# Calculate the maximal gap and minimal gap
    if abs(gap_value) > max_gap:
        max_gap = abs(gap_value)
    if abs(gap_value) < min_gap:
        min_gap = abs(gap_value)
# Calculate the distinct digits
    distinct_digits[caldistinctdigit(i)] += 1

    tuple_first_and_last = (getfirst(i), getlast(i))
    if tuple_first_and_last in dic_reminder:
        dic_reminder[tuple_first_and_last] += 1
    else:
        dic_reminder.setdefault(tuple_first_and_last, 1)

for key in dic_reminder:
    if dic_reminder[key] == max(dic_reminder.values()):
        first_and_last.add(key)

print(f'\nThere are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()

    
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')

print('\nThe minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')

print('\nThe number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
        
