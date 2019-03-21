# Written by Di Peng for COMP9021
import os.path
import sys
from collections import deque

tunnel_input = list()
tunnel_list = list()
the_distance_from_west = 0
try:
    filename = input('Please enter the name of the file you want to get data from: ')
    with open(filename) as program_file:
        for line in program_file:
            if not line.isspace():
                tunnel_list.append([int(i) for i in line.split()])
    if len(tunnel_list) != 2:
        raise ValueError
    if len(tunnel_list[0]) != len(tunnel_list[1]):
        raise ValueError
    if len(tunnel_list[0]) < 4 and len(tunnel_list[1]) < 4:
        raise ValueError
    for i in range(len(tunnel_list[0])):
        if tunnel_list[0][i] < tunnel_list[1][i]:
            raise ValueError
except FileNotFoundError:
    print('Sorry, there is no such file. ')
    sys.exit()
except TypeError:
    print('Sorry, input file does not store valid data. ')
    sys.exit()
except ValueError:
    print('Sorry, input file does not store valid data. ')
    sys.exit()
    

upper_minimum = tunnel_list[0][0]
lower_maximum = tunnel_list[1][0]
record_distance = 0

for i in range(len(tunnel_list[0])):
    if upper_minimum > tunnel_list[0][i]:
        upper_minimum = tunnel_list[0][i]
    if lower_maximum < tunnel_list[1][i]:
        lower_maximum = tunnel_list[1][i]
    if upper_minimum <= lower_maximum:
        break
    else:
        record_distance += 1

the_distance_from_west = record_distance

record_list = list()
for i in range(len(tunnel_list[0])):
    record_distance = 0
    upper_minimum = tunnel_list[0][i]
    lower_maximum = tunnel_list[1][i]
    for j in range(i, len(tunnel_list[0])):
        if upper_minimum > tunnel_list[0][j]:
            upper_minimum = tunnel_list[0][j]
        if lower_maximum < tunnel_list[1][j]:
            lower_maximum = tunnel_list[1][j]
        if upper_minimum <= lower_maximum:
            break
        else:
            record_distance += 1
    record_list.append(record_distance)

'''
the_next_first_upper = first_upper
the_next_first_lower = first_lower
inside_tunnel_list = list()
record_upper_index = 0
record_lower_index = 0
for i in range(1, len(tunnel_list[0])):
    upper_minimum = the_next_first_upper
    lower_maximum = the_next_first_lower
    if the_next_first_upper > tunnel_list[0][i]:
        upper_minimum = tunnel_list[0][i]
    if the_next_first_lower < tunnel_list[1][i]:
        lower_maximum = tunnel_list[1][i]
    if lower_minimum >= upper_maximum:
        record_upper_index = i
'''    
print('From the west, one can see into the tunnel over a distance of', the_distance_from_west, end='.\n')
print('Inside the tunnel, one can see into the tunnel over a maximum distance of', max(record_list), end='.\n')
