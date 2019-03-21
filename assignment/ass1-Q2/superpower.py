# Written by Di Peng for COMP9021

import sys
import copy
import datetime

# Finding the power of the same hero many times
# Switching the minmum number in list
# Calculating the sum of this list
def maxPowerManyTimes(L, loop_times):
    L2 = copy.copy(L)
    number = count
    for times in range(0, loop_times):
        min_digit = min(L2)
        L2[L2.index(min_digit)] *= -1
    return sum(L2)

# Finding the power of the same hero at most once
# Switching the minmum number in list1 and put it in list2
# Removing this number in list1
# Calculating the sum of list2
def maxPowerOneTime(L, loop_times):
    L2 = copy.copy(L)
    L3 = []
    for times in range(0, loop_times):
        min_digit = min(L2)
        L3.append(min_digit*-1)
        L2.remove(min_digit)
    L3 += L2
    return sum(L3)

def maxPowerConsecutiveHero(L, loop_times):
    power_of_sum = []
    for i in range(0, len(L) - loop_times + 1):
        number = count
        for times in range(i, i + loop_times):
            number = number + -1 * 2 * L[times]
        power_of_sum.append(number)
    return max(power_of_sum)

def maxPowerArbitrarilyConsecutive(L):
    power_of_sum = []
    power_of_sum.append(count)
    for i in range(0, len(L)):
        number = count
        if L[i] < 0:
            for times in range(i, len(L)):
                number = number + -1 * 2 * L[times]
                if number > power_of_sum[0]:
                    power_of_sum.append(number)
                else:
                    break
    return max(power_of_sum)
    
try:
    heroes_powers_input = input('Please input the heroes\' powers: ')
    heroes_powers = [int(number) for number in heroes_powers_input.split()]
    if len(heroes_powers) <= 0:
        raise ValueError
except ValueError:
    print('Sorry, these are not valid power values. ')
    sys.exit()
try:
    nb_of_switches = int(input('Please input the number of power flips: '))
    if len(heroes_powers) < nb_of_switches:
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
count = sum(heroes_powers)
print('Possibly flipping the power of the same hero many times, the greatest achievable power is', maxPowerManyTimes(heroes_powers, nb_of_switches), end = '.\n')
print('Flipping the power of the same hero at most once, the greatest achievable power is', maxPowerOneTime(heroes_powers, nb_of_switches), end = '.\n')
print('Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is', maxPowerConsecutiveHero(heroes_powers, nb_of_switches), end = '.\n')
print('Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is', maxPowerArbitrarilyConsecutive(heroes_powers), end = '.\n')
