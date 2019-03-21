# Written by Di Peng for COMP9021

import sys

try:
    file_name = str(input('Which data file do you want to use? '))
    decilitres_of_water = int(input('How many decilitres of water do you want to pour down? '))
    if decilitres_of_water < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up. ')
    sys.exit()
    
L = []
key_list = []
value_list = []
highest_water_level = 0
highest_water_level_list = [0]
key_gap = 0
value_gap = 0
height = 0
water_level_list = []

try:
    with open(file_name) as Rain_program_file:
        for line in Rain_program_file:
            for digit in line.split():
                if digit.isspace():
                    continue
                L.append(int(digit))
except FileNotFoundError:
    print('File not found, giving up. ')
    sys.exit()

L = sorted(L)
land_dic = {}

for i in L:
    if i in land_dic:
        land_dic[i] += 1
    else:
        land_dic.setdefault(i, 1)

for key in land_dic:
    key_list.append(key)
    value_list.append(land_dic[key])

for i in range(0, len(key_list)):
    if i < len(key_list) - 1:
        key_gap = key_list[i+1]-key_list[i]
    value_gap += value_list[i]
    highest_water_level += key_gap * value_gap
    highest_water_level_list.append(highest_water_level)
    if decilitres_of_water == 0:
        height = value_list[0]
        break
    if decilitres_of_water <= value_list[-len(key_list)] * key_gap:
        height = key_list[-len(key_list)] + decilitres_of_water/value_gap
        break
    if decilitres_of_water <= highest_water_level or i == len(key_list)-1:
        height = key_list[i] + (decilitres_of_water - highest_water_level_list[i])/value_gap
        break
    
print(f'The water rises to {height:.2f} centimetres.')
