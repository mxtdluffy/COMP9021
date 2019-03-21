# Written by Di Peng for COMP9021

import os.path
import sys

from collections import defaultdict

cable_car = list()
try:
    filename_input = input('Please enter the name of the file you want to get data from: ')
    with open(filename_input) as program_file:
        for line in program_file:
            cable_car.extend(line.split())
except FileNotFoundError:
    print('Sorry, there is no such file. ')
    sys.exit()

# Judging whether the content of file is digit, positive integer and sorted
try:
    if len(cable_car) < 2:
        raise ValueError
    if not all(cable_car[i].isdigit() and int(cable_car[i]) > 0
               and int(cable_car[i]) < int(cable_car[i+1])
               for i in range(len(cable_car) - 1)):
        raise ValueError
    if not cable_car[-1].isdigit() and int(cable_car[-1]) > 0:
        raise ValueError
    cable_car_list = [int(a) for a in cable_car]
except ValueError:
    print('Sorry, input file does not store valid data. ')
    sys.exit()

gap_of_cable_car_list = defaultdict(list)
item = list()
maximum_count = 0
for i in range(1, len(cable_car_list) - 1):
    gap = cable_car_list[i] - cable_car_list[i-1]
    if cable_car_list[i-1] and cable_car_list[i] not in item:
        item.append(cable_car_list[i-1])
        item.append(cable_car_list[i])
    if cable_car_list[i+1] - cable_car_list[i] == gap:
        item.append(cable_car_list[i+1])
    else:
        item = []
    if maximum_count < len(item):
        maximum_count = len(item)
'''
gap_of_cable_car_list = list()
item = list()
maximum_count = 0
for i in range(len(cable_car_list) - 1):
    gap_of_cable_car_list.append(
            cable_car_list[i+1]-cable_car_list[i])

maximum_count = max(j2 - j1 + 1
    for j1 in range(len(gap_of_cable_car_list))
        for j2 in range(j1, len(gap_of_cable_car_list))
            if gap_of_cable_car_list[j1:j2+1]==[gap_of_cable_car_list[j1]]*(j2-j1+1)
    )
'''
i = 0
j = 1
the_rest_pillars_max = 0
item = 0
while i < len(cable_car_list) - the_rest_pillars_max:
    '''
    item = []
    gap = cable_car_list[j] - cable_car_list[i]
    if cable_car_list[i] and cable_car_list[j] not in item:
        item.append(cable_car_list[i])
        item.append(cable_car_list[j])
    while item[-1] + gap in cable_car_list:
        item.append(item[-1] + gap)
    if the_rest_pillars_max < len(item):
        the_rest_pillars_max = len(item)
    print(item)
    if j < len(cable_car_list)/3:
        j += 1
    else:
        i += 1
        j = i + 1
    '''
    gap = cable_car_list[j] - cable_car_list[i]
    item = 2
    remainder = cable_car_list[j]
    while remainder + gap in cable_car_list:
        remainder += gap
        item += 1
    if the_rest_pillars_max < item:
        the_rest_pillars_max = item
    if j < len(cable_car_list)/3:
        j += 1
    else:
        i += 1
        j = i + 1
    
if maximum_count == len(cable_car_list):
    print('The ride is perfect!')
else:
    print('The ride could be better...')
print('The longest good ride has a length of:', maximum_count-1)
print('The minimal number of pillars to remove to build a perfect ride from the rest is:', len(cable_car_list) - the_rest_pillars_max)
